menu = "idli,dosa,chai"
#menu ek list hai 

name = input("Can I know Your Name Sir\n")
#input name ka hoga input will be taken from the user who is running the proggrame

print("Hello Mr." + name  + " here's the menu " + menu)
#name = xyz 

#what do you mean by elif func.
#else if = agar yeh


order = input("type your order Mr." + name +  "\n")


if order == "idli":
    price = 75

elif order == "dosa":
    price = 65

elif order == "chai":
    price = 15

quantity = input("Mr." +name+ " what should be the quantity of the " +order+"\n")

Total = int(price)*int(quantity)

print("your Total will be " + str(Total) + "$")


