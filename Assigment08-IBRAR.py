# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# IBRAR,3.9.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []
strChoice = None


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        __str__(self)
        add_data_to_list(self, list_of_rows)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        IBRAR,3.9.2021,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class (Done)
    # constructor
    def __init__(self, name, price):
        # attributes
        self.__name = str(name)
        self.__price = float(price)

    # properties
    @property  # getter for product name
    def name(self):
        return str(self.__name).title()

    @name.setter  # setter for product name
    def name(self, value):
        self.__name = value

    @property  # getter for price
    def price(self):
        return str(self.__price)

    @price.setter  # setter for price
    def price(self, value):
        self.__price = value

    # Method
    def __str__(self):
        """Return product data as a string"""
        return self.name + "," + self.price

    def add_data_to_list(self, list_of_rows):
        row = Product(self.__name, self.__price)
        list_of_rows.append(row)
        return list_of_rows, "\nThe data has been added to the list!\n"

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> (saves list of product objects)

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        IBRAR,3.9.2021,Modified code to complete assignment 8
    """
    # TODO: Add Code to save data to a file (Done)
    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Writes data from the list of dictionary rows in a file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want written in the file:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row.name + "," + str(row.price) + "\n")
        file.close()
        return "\nData successfully saved to the file!\n"

    # TODO: Add Code to read data from a file (Done)
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows containing product objects
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")  # read data from file
            for line in file:
                name, price = line.split(",")
                row = Product(name.strip(), price.strip())
                list_of_rows.append(row)
        except FileNotFoundError:
            file = open(file_name, "w")  # create a new file if no such file exists
        file.close()
        return list_of_rows
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring (Done)
    """ Performs Input and Output tasks
    methods:
        print_menu_choice()
        input_menu_choice()
        print_current_data_in_list(list_of_rows) -> (a list of product objects)
        input_new_product_data()

    changelog: (When,Who,What)
        IBRAR,3.9.2021, Added code
    """
    # TODO: Add code to show menu to user (Done)
    @staticmethod
    def print_menu_choice():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
Menu of Options
    1) View current product data
    2) Add new product data
    3) Save Data to File
    4) Exit Program    
        ''')

    # TODO: Add code to get user's choice (Done)
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    # TODO: Add code to show the current data from the file to user (Done)
    @staticmethod
    def print_current_data_in_list(list_of_rows):
        """ Shows the current data in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        if list_of_rows == []:
            print("\nThe file contains no data!")
        else:
            print()
            print("******* The Current Product Data is: *******")
            for row in list_of_rows:
                print(row.name + "," + str(row.price))
            print("*******************************************")
            print()

    # TODO: Add code to get product data from user (Done)
    @staticmethod
    def input_new_product_data():
        """ Gets a new product and price from the user

        :return: (object) containing user input
        """
        name = str(input("Please enter a product name: ")).strip()
        if name.isnumeric():
            raise Exception("Product name cannot be only numbers!")
        else:
            try:
                price = float(input("Please enter a product price: "))
                return name, price
            except ValueError:
                print("Error: Price must be only numbers!")


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body (Done)
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data

while True:

    IO.print_menu_choice()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    if strChoice.strip() == "1":  # Show user current data
        IO.print_current_data_in_list(lstOfProductObjects)

    elif strChoice.strip() == "2":  # Add new product data
        try:
            new_name, new_price = IO.input_new_product_data()
            new_data = Product(new_name, new_price)
            print(new_data.add_data_to_list(lstOfProductObjects)[1])
        except Exception as e:
            print("Error: " + str(e))

    elif strChoice.strip() == "3":  # Save data and exit
        print(FileProcessor.save_data_to_file(strFileName, lstOfProductObjects))

    elif strChoice.strip() == "4":
        break
# Main Body of Script  ---------------------------------------------------- #
