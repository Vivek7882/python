#create a program into minitue into hour
#ex 130=2hour and 10 minitue


time=input("enter time:")
time=int(time)

hour=time//60
min=time%60

print(hour,'hour',min,'minite')