#write a program to calculate compound interest using lambda function 

getcom=lambda p,r,t: p*(1+r/100) ** t-p

p=float(input("enter price:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))

ci=getcom(p,r,t)

amount=ci+p


print("compound",ci)
print("total amount",amount)