username = input("Username : ")
password = input("Password : ")
if username == "guest" and password == "1234":
    print("Login Success")
    print("----- Welcome to water shop -----")
    print("1. น้ำเปล่า                                 ราคา 10 บาท/1 ขวด")
    print("2. น้ำแข็ง                                 ราคา 3 บาท/1 ถุง")
    print("3. น้ำเปล่าแบบสะอาด                        ราคา 35 บาท/1 ขวด")
    print("4. น้ำเปล่าแต่มีปลาในน้ำ                      ราคา 100 บาท/1 ถุง")
    print("--------------------------------------------------------")
    user = int(input("ท่านลูกค้าต้องการสินค้าหมายเลข >> "))
    if user == 1:
        am = int(input("ต้องการ น้ำเปล่า ราคา 10 บาท จำนวนกี่ขวดค่ะ >> "))
        print("ราคารวมทั้งหมด คือ "+str(am * 10)+" บาท")
    elif user == 2:
        am = int(input("ต้องการ น้ำแข็ง ราคา 3 บาท จำนวนกี่ถุงค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(am * 3) + " บาท")
    elif user == 3:
        am = int(input("ต้องการ น้ำเปล่าแบบสะอาด ราคา 35 บาท จำนวนกี่ขวดค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(am * 35) + " บาท")
    elif user == 4:
        am = int(input("ต้องการ น้ำเปล่าแต่มีปลาในน้ำ ราคา 100 บาท จำนวนกี่ถุงค่ะ >> "))
        print("ราคารวมทั้งหมด คือ " + str(am * 100) + " บาท")
    else :
        print("ไม่มีรหัสสินค้าในรายการ")
else:
    print("Username or Password is Incorrect.")