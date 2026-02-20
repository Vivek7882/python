#write a program to calculate fahrenheit of given celsius using lambda function 

getfahrenheit=lambda f : (f-32)*5/9

f=float(input("enter fahrenheit:"))

print(getfahrenheit(f))