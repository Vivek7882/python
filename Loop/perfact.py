#write a program to figure out whether given number  is perfect number or not

num=int(input("enter number:"))
i=1
sum=0

while i<num:
    if num%i==0:
         sum=sum+i
    i=i+1

if sum==num:
     print("number is perfact")
else:
     print("number is not perfact")