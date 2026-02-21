#write a program to figure out hexadcimal of given decimal number 


def tobinary(number):
    if number>0:
        reminder=number%16
        number=number//16
        tobinary(number)
        print(reminder,end=" ")


number=int(input("enter number:"))
tobinary(number)