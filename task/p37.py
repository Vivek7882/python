#Write a program to calculate discount amount using price and discount rate.

p=int(input("enter price:"))
r=int(input("enter rate:"))

ans=p*r/100
final=p-ans

print("dicount price:",final)
