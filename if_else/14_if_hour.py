"""write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input """

hour=int(input("enter hour:"))

if hour>12 and hour<=24:
    print("hour is",(hour-12),"PM")

if hour<=12:
    print("hour is",hour,"AM")

if hour>24:

    print("envalid hour")
