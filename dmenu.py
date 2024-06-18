import readrecord, addrecord, updaterecord, deleterecord, report
 
# create a function to read content froms the dbMenu.txt file
def read_file():
    try:
        with open("PYTHON/Python Project/dbMenu.txt") as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print(f"Error handling file because: {fnf}")
 
def films_menu():
    option = 0 # declared option variable and initialised with an integer data type
    # declared options_list variable and initialised with a list data structure with string items
    options_list = ["1","2","3","4","5","6"]
 
    # declared the menu_choices variable and initialised with the read_file() function
    menu_choices = read_file()
 
    # Create a while loop repeat the code within the body of thw while condition
    while option not in options_list:
        # repeatedly call/invoke the read_file() function whihc is initialised with the menu_choices variable
        print(menu_choices)
 
 
        # re-assign the option variable wiht a new value
        option = input("Enter an option from the menu choices above ")
        if option not in options_list:
            print(f"{option} is not a valid choice! ")
    return option
 
 
main_program = True # declare main_program and initialised with a boolean data type with a value of True
 
while main_program: # same as while True
   
    # declared the main_menu variable and initialised with the films_menu() function
    main_menu = films_menu()
 
    match main_menu:
        # if  case value =  ( option = input("Enter an option from the menu choices above ")) the value 1
        case "1":
            readrecord.read_record()
        case "2":
            addrecord.add_record()
        case "3":
            updaterecord.update_record()
        case "4":
            deleterecord.delete_record()
        case "5":
            report.search_report()
        case _:
            # re-assign the main_program variable with a boolean False value
            main_program = False
input("Press 'Enter' to exit the Menu/App")