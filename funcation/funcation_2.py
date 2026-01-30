#write a program to create function that convert given fahrenheit into celsius 

def getF (f):
    c=(f-32)*5/9
    return c


n=int(input("enter number:"))
result=getF(n)
print(result)



