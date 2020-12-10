# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <ARalevski>,<12.05.20>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strStatus = ''
strChoice = ''


# Processing  --------------------------------------------------------------- #
class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <ARalevski>,<12.05.20>,Modified code to complete assignment 8
    """
    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception('Error setting initial values \n' + str(e))

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value: str):
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception('Product names cannot be numbers!')

    # -- Properties --
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception('Product price must contain numbers!')

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <ARalevski>,<12.05.20>,Modified code to complete assignment 8
    """

    # Read data from a file
    @staticmethod
    def read_data_from_file(file_name):
        list_of_rows = []
        file = open(file_name, 'r')
        for line in file:
            data = line.split(',')
            row = Product(data[0], data[1])
            list_of_rows.append(row)
        file.close()
        print(list_of_rows)
        return list_of_rows

    # Save data to a file
    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        file = open(file_name, 'w')
        for product in lstOfProductObjects:
            # obj1 = Product()
            file.write(product.to_string() + '\n')
            file.close()
        return lstOfProductObjects

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """
    # Show menu to user
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File 
        3) Exit Program
        ''')
        print()

    # Get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()
        return choice

    # Show the current data from the file to user
    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
             print(row.product_name + ", " + '$' + str(row.product_price))
        print("*******************************************")
        print()

    # Get product data from user
    @staticmethod
    def input_new_product_and_price():
        strproduct = str(input('Enter a Product: ').strip())
        fltprice = float(input('Enter a price for the Product: ').strip())
        p = Product(product_name=strproduct, product_price=fltprice)
        return p

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

# Main Body of Script  ---------------------------------------------------- #
# Step 1- Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName)

# Step 2- Display a menu of choices to the user
while True:
    # Show user current data in the list of product objects
    # IO.print_current_products_in_list(lstOfProductObjects)
    # Display a menu of choices to the user
    IO.print_menu()
    IO.print_current_products_in_list(lstOfProductObjects)
    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Step 3 - Process user's menu choice
    # Let user add data to the list of product objects
    if strChoice.strip() == '1':
        # strproduct, fltprice = IO.input_new_product_and_price()
        lstOfProductObjects.append(IO.input_new_product_and_price())
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    #Step 4- Let user save current data
    elif strChoice == '2':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    # Step 5- Let user read current data
    # elif strChoice == '3':
    #     print("Warning: Unsaved Data Will Be Lost!")
    #     strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
    #     if strChoice.lower() == 'y':
    #         FileProcessor.read_data_from_file(strFileName)
    #         IO.input_press_to_continue(strStatus)
    #     else:
    #         IO.input_press_to_continue("File Reload  Cancelled!")
    #     continue  # to show the menu

    #Step 6- Let user exit program
    elif strChoice == '3':
        print("Goodbye!")
        break

