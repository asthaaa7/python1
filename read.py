def read_file():
    file = open("laptop.txt","r")
    laptop_dictionary = {}
    laptop_id = 1

    for line in file:
        line = line.replace("\n","")
        laptop_dictionary.update({laptop_id: line.split(",")})
        laptop_id = laptop_id + 1
    file.close()
    return laptop_dictionary

def display_stock():
    file = open("laptop.txt", "r")
    a = 1
    for line in file:
        print("|" ,a, "\t\t" + line.replace(",","\t\t"))
        a = a+1
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")
