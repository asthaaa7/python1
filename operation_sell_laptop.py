import read
import write
from datetime import datetime

def read_laptop_no():
    select_laptop_no = False
    laptop_no = 0
    while select_laptop_no == False:
        try:
            laptop_no = int(input("Please enter the number of laptop you want to purchase."))
            select_laptop_no = True
        except:
            print("Invalid number.Please enter valid number of laptop you want to buy!")
        print("\n")
    return laptop_no

def read_laptop_id():
    select_laptop_id = False
    id_laptop_bought = -1
    while select_laptop_id == False:
        try:
            id_laptop_bought = int(input("Please specify the laptop ID that you wish to purchase:"))
            select_laptop_id = True
        except:
            print("The selected option is unavailable. Please enter one of the valid laptop IDs.")
    print("\n")

    return id_laptop_bought

def sell_laptop():
    bought_laptop = {}
    more_laptop = True

    print("------------------------------------------------------------------------------------")
    print("Enter the customer's details to produce a bill.")
    print("------------------------------------------------------------------------------------")
    print("\n")

    name = input("Type the client's name here:")
    print("\n")
    phn_num = input("Enter the customer's phone number here:")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------")
          

    while more_laptop == True:
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("ID. \t\t\t \tLaptop  \t\t\t \tCompany Name \t\t\t Price \t\t\ \tQuantity \t\t \tGraphics ")
        print("---------------------------------------------------------------------------------------------------------------------------")

        read.display_stock()

        laptop_ID_bought = read_laptop_id()

        #Valid laptop Id
        laptop_dictionary = read.read_file()
        print(laptop_dictionary)
        while laptop_ID_bought <= 0 or laptop_ID_bought>len(laptop_dictionary):
            print("Invalid ID.Please provide laptop id which is valid!!!")
            print("\n")

            laptop_ID_bought = read_laptop_id()
            
        laptops_number = read_laptop_no()

        #Valid Quantity of laptop
        get_number_of_laptop = int(laptop_dictionary[laptop_ID_bought][3])

        print(get_number_of_laptop)
        print(type(get_number_of_laptop))
        if get_number_of_laptop == 0:
            print("Oops sorry! This laptop is out of stock.")
            continue
            #id_laptop_bought = read_id_of_laptop()

        while laptops_number < 0 or laptops_number > int(get_number_of_laptop):
            print("Sorry! We do not have the quantity of laptop you are searching for..")
            print("\n")
            laptops_number = read_laptop_no()

        #Updating the text file
        laptop_dictionary[laptop_ID_bought][3] = int(laptop_dictionary[laptop_ID_bought][3]) - int(laptops_number)
        write.update_quantity(laptop_dictionary)
        
        #Getting user purchase items
        products_name = laptop_dictionary[laptop_ID_bought][0]
        chosen_quantity = laptops_number
        unit_price = laptop_dictionary[laptop_ID_bought][2]
        price_of_chosen_laptop = laptop_dictionary[laptop_ID_bought][2].replace("$",'')
        gross_price = int(price_of_chosen_laptop) * int(chosen_quantity)
        print(bought_laptop)
        
        if laptop_ID_bought in bought_laptop:
            bought_laptop[laptop_ID_bought] = [products_name,chosen_quantity+bought_laptop[laptop_ID_bought][1],unit_price,gross_price+bought_laptop[laptop_ID_bought][3]]
        else:
            bought_laptop[laptop_ID_bought] = [products_name,chosen_quantity,unit_price,gross_price]
        print(bought_laptop)
        continue_buying = input("Do you want to continue(Y/N)?").upper()

        if continue_buying == "YES" or continue_buying == "Y":
            more_laptop = True

        else:
            more_laptop = False
            gross_cost_of_laptop = 0
            shipping_cost = 200
            for i, key in   enumerate(bought_laptop):
                gross_cost_of_laptop += int(bought_laptop[key][3])
            grand_total = gross_cost_of_laptop + shipping_cost
            today_date_and_time = datetime.now()

            write.display_bill(name,phn_num,today_date_and_time,bought_laptop,shipping_cost,grand_total)
            write.print_bill(name,phn_num,today_date_and_time,bought_laptop,shipping_cost,grand_total)
            
        
def purchase_laptop():

    laptop_purchased = {}
    more_laptop = True

    print("---------------------------------------------------------------------------------------------------------------------------")
    print("Enter the retailer's information to create a bill.")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    name_of_retailer = input("Type the retailer's name here:")
    print("\n")
    phone_number = input("Enter the retailer's phone number here:")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------")
          

    while more_laptop == True:
        print("Available stock:")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \t\t Laptop Name \t\t\t Company Name \t\t\t Price \t\t\ Quantity \t\t Graphics ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

        read.display_stock()

        purchased_laptop_id = read_laptop_id()

        #Valid laptop Id
        laptop_dictionary = read.read_file()
        print(laptop_dictionary)
        while purchased_laptop_id <= 0 or purchased_laptop_id>len(laptop_dictionary):
            print("Please provide a valid laptop id!!!")
            print("\n")

            purchased_laptop_id = read_laptop_id()
            
        num_of_laptop = read_laptop_no()

        

        #Updating the text file
        laptop_dictionary[purchased_laptop_id][3] = int(laptop_dictionary[purchased_laptop_id][3]) + int(num_of_laptop)
        write.update_quantity(laptop_dictionary)
        
        #Getting user purchase items
        name_of_the_product = laptop_dictionary[purchased_laptop_id][0]
        selected_quantity = num_of_laptop
        unit_price = laptop_dictionary[purchased_laptop_id][2]
        price_of_selected_laptop = laptop_dictionary[purchased_laptop_id][2].replace("$",'')
        gross_price = int(price_of_selected_laptop) * int(selected_quantity)
        
        
        if purchased_laptop_id in laptop_purchased:
            laptop_purchased[purchased_laptop_id] = [name_of_the_product,selected_quantity+laptop_purchased[purchased_laptop_id][1],unit_price,gross_price+laptop_purchased[purchased_laptop_id][3]]
        else:
            laptop_purchased[purchased_laptop_id] = [name_of_the_product,selected_quantity,unit_price,gross_price]
        print(laptop_purchased)
        continue_buying = input("Do you want to continue(YES/NO)?").upper()

        if continue_buying == "YES" or continue_buying == "Y":
            more_laptop = True

        else:
            more_laptop = False
            gross_cost_of_laptop = 0
            for i, key in   enumerate(laptop_purchased):
                gross_cost_of_laptop += int(laptop_purchased[key][3])
            VAT = 0.13 * gross_cost_of_laptop
            grand_total = gross_cost_of_laptop + VAT
            today_date_and_time = datetime.now()

            write.display_purchase_bill(name_of_retailer,phone_number,today_date_and_time,laptop_purchased,VAT,grand_total)
            write.print_bill(name_of_retailer,phone_number,today_date_and_time,laptop_purchased,VAT,grand_total)
                   
        
            
        
        
