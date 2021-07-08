print("=========computer Bazar========")
model = input("enter the computer model")
model = int(model)
if model == 1:
    print("1.dell(20000)")
    cost1 = int(20000)
elif model == 2:
    print("2.mac(50000)")
    cost1 = int(50000)
elif model == 3:
    print("3.toshiva(30000)")
    cost1 = int(35000)
else:
    print("enter options 1 to 3")
quantity = input("Enter the quantity")
quantity = int(quantity)
print(quantity)
delivery_option = input("enter 1 for home delivery and 2 for pick up")
print(delivery_option)
delivery_option = int(delivery_option)
if delivery_option == 1:
    print("delivery charge is 1000")
    cost2 = int(cost1 + 1000)
elif delivery_option == 2:
    print("free delivery")
    cost2 = int(cost1)
else:
    print("enter valid number")
packing = input("enter the packing options")
packing = int(packing)
if packing == 1:
    print("plastic(500)")
    cost3 = int(500)
elif packing == 2:
    print("bag(1000)")
    cost3 = int(1000)
elif packing == 3:
    print("gift box(5000)")
    cost3 = int(5000)
else:
    print("enter number between 1 to 3")
location = input("enter the delivery location 1 for ktm, 2 for Lkt and 3 for Bkt")
location = int(location)
if location == 1:
    print("13% vat is added")
    tax_price = float(quantity * cost1*0.13)
    print(f"total tax amount is: {tax_price}")
    cost4 = float(tax_price)
elif location == 2:
    print("free")
    cost4 = int(0)
elif location == 3:
    print("Free")
    cost4 = int(0)
else:
    print("invalid location")
grand_total = float(cost1 * quantity + cost2 + cost3 + cost4)
print(f"Grant Total amount is: {grand_total}")
