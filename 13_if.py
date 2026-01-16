#create a program to profit and loss for sell and purchas price using if statement

purchas_price=float(input("enter purchas price:"))
sell_price=float(input("enter sell rpice:"))

different=sell_price-purchas_price

if different > 0:
    print("profit is:",different)

if different<0:
    print("lose is:",different)

if different==0:
    print("no profit and no lose")