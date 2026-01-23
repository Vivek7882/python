# write a program to find out whether given year is leap year or not
# https://www.wikihow.com/Calculate-Leap-Years

year=int(input("enter year:"))

if year<1:
    print("envalid year")

else:
    remainder1=year%4
    remainder2=year%100
    remainder3=year%400

    if remainder1==0 and remainder2!=0:
        print("this year is leap year")

    elif remainder2==0 and remainder3==0:
        print("this year is leap year")

    else:
        print("this year is not leap year")