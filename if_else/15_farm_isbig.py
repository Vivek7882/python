#write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 

length1=float(input("enter 1th length:"))
width1=float(input("enter 1th width:"))

length2=float(input("enter 2th length:"))
width2=float(input("enter 2th width:"))

area1=length1*width1
area2=length2*width2

if area1>area2:
    print("1th farm is bigger")

if area1<area2:
    print("2th farm is bigger")