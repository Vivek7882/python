''' Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------'''
sub1=float(input("enter sub 1 mark:"))
sub2=float(input("enter sub 2 mark:"))
sub3=float(input("enter sub 3 mark:"))
sub4=float(input("enter sub 4 mark:"))
sub5=float(input("enter sub 5 mark:"))

total=sub1+sub2+sub3+sub4+sub5

avg=total/5

if avg>=90 and avg<=100:
    print("grade is A+")

elif avg>=80 and avg<=89:
    print("grade is A")

elif avg>=70 and avg<=79:
    print("grade is B")

elif avg>=60 and avg<=69:
    print("grade is C")

elif avg>=50 and avg<=59:
    print("grade is D")

else:
    print("need to improve")
    







