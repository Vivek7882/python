#write a program to figure out whether given number  is prime number or not

import sys
number=int(input("enter number:"))
divsor=2

while divsor<number:
    remainder=number%divsor
    if remainder==0:
        print("number is not prime")
        sys.exit(1)

    else:
        divsor=divsor+1

print("number is prime")