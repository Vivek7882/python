# Write a program to calculate total amount after simple interest.
p=int(input("enter principal:"))
r=int(input("enter rate:"))
t=int(input("enter time in year:"))

ans=p*r*t/100

ans2=ans+p

print(ans2)