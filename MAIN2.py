import read
import operation_sell_laptop

print("\n")
print("\n")
print("\t \t \t \t \t \t \t \tOur Electronics ")
print("\n")
print("\t \t \t \t \tBudhanilkantha, Kathmandu | Contact No: 9862345600,9808029495")
print("\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t \t \tNamaste! Welcome to the system. Have a good day ahead!!")
print("----------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")
loop_p = True
while loop_p == True:
    print("Type '1' to sell laptops")
    print("Type '2' to purchase laptops")
    print("Type '3' to exit the system")
    print("\n")

    action_choice = False
    while action_choice == False:
        try:
            chosen_action = int(input("To continue enter an option."))
            action_choice = True
        except:
            print("Invalid Option!!. Please chose a valid option.")

    if chosen_action == 1:
        print("Thank you for choosing to sell laptop.")
        operation_sell_laptop.sell_laptop()
        print("\n")
        print("\n")
        
    elif chosen_action == 2:
        print("Thank you for choosing to purchase laptop.")
        operation_sell_laptop.purchase_laptop()
        print("\n")
        
    elif chosen_action == 3:
        print("Thank you for visiting. Have a great day!!")
        loop_p = False
        print("\n")
        
    else:
        print("Invalid option!! Please try choosing a correct option.")
