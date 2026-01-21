'''
write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.'''

num1=float(input("enter first number:"))
num2=float(input("enter secound number:"))

choice=input('enter your choice:')

if choice=='+':
    print("sum is:",(num1+num2))

elif choice=='-':
    print("sub is:",(num1-num2))

elif choice=='*':
    print("mul is:",(num1*num2))

elif choice=='/':
    print("div is:",(num1/num2))


