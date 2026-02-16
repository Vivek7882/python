def getMerit(computer,drawing,english,history,maths,science):
    total=history+maths+science
    return total

c = int(input("Enter marks for computer: "))
d = int(input("Enter marks for drawing: "))
e = int(input("Enter marks for english: "))
h = int(input("Enter marks for history: "))
m = int(input("Enter marks for maths: "))
s = int(input("Enter marks for science: "))

total=getMerit(maths=m,english=e,drawing=d,history=h,science=s,computer=c)

print(total)