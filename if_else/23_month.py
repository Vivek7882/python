''' write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days '''

month=int(input("enter month 1 to 12:"))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("this month is 31 days")

elif month==2:
    print("this is 28 and 29 days")

else:
    print("this month is 30 days")