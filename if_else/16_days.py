"""write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)
            input 1 : monday 
            input 2 : tuesday 
            input 7 : sunday """

num=int(input("enter number:"))

if num==1:
    print("monday")

if num==2:
    print("tuesday")
if num==3:
    print("Wednesday")

if num==4:
    print("Thursday")

if num==5:
    print("Friday")

if num==6:
    print("Saturday")
if num==7:
    print("sunday")

if num>7 or num<=0:
    print("envali number")