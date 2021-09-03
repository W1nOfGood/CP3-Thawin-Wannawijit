def login():
    UI = input("Username: ")
    PI = input("Password: ")
    if UI == "guest" and PI == "1234":
        return showMenu()
    else:
        print("Incorrect Password or Username")
        return login()
def showMenu():
    print("----- Something Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. exit")
    return menuSelect()
def menuSelect():
    US = int(input("Select a menu: "))
    if US == 1:
        PV = int(input("How much is the menu: "))
        print("Menu + Vat7% = ",vatCalculator(PV))
        return menuSelect()
    elif US == 2:
        print("Menu + Vat7% = ",priceCalculator())
    elif US == 3:
        return exit()
    else:
        print("Please select the menu with the numbers")
        return menuSelect()
def vatCalculator(totalPrice):
    V = 7
    RS = totalPrice + (totalPrice * V / 100)
    return RS
def priceCalculator():
    p1 = int(input("First Product Price: "))
    p2 = int(input("Second Product Price: "))
    sum = p1 + p2
    print("Menu without Vat7% = ",sum)
    return vatCalculator(p1 + p2)
    

login()