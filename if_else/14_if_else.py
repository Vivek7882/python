## write a program to find out which is cheaper product to purchase from 2 product's weight and price.

weight1=float(input("enter weight of 1st product:"))
price1=float(input("enter price of  1th product:"))

weight2=float(input("enter weight of 2th product:"))
price2=float(input("enter price of 2th product:"))


ans1=price1/weight1
ans2=price2/weight2

if ans1<ans2:
    print("1st product is cheaper")

else:
    print("2nd product is cheaper")