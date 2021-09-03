def vatCal(total):
    result = total+(total*7/100)
    return result

total2 = int(input("ราคา: "))
print(vatCal(total2))