#write a program to figure out octal of given decimal number 

def tobinary(number):
    if number>0:
        reminder=number%8
        number=number//8
        tobinary(number)
        print(reminder,end=" ")


number=int(input("enter number:"))
tobinary(number)