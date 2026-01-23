# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 

weight1=float(input("enter weight of 1st product:"))
price1=float(input("enter price of  1th product:"))

weight2=float(input("enter weight of 2th product:"))
price2=float(input("enter price of 2th product:"))

if price1<=0 or price2<=0 or weight1<=0 or weight2<=0:
    print("negative and zero value is not allow")

else:
    ans1=price1/weight1
    ans2=price2/weight2

    if ans1<ans2:
        print("1st product is cheaper",(ans2-ans1))

    else:
        print("2nd product is cheaper",(ans1-ans2))