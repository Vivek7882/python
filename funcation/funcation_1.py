# concept of user defined function

def getSuare (number):
    s=number*number
    return s

def getcube (num):
    q=getSuare(num)*num
    return q


n=int(input("enter number:"))

result=getSuare(n)
print("squart:",result)# calling funcation
result1=getcube(n)
print("cube:",result1)