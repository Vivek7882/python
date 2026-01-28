#write a program to count digits in given string 

s = input("Enter a string: ")
count = 0

for item in s:
     if item.isdigit():  #isdifit is use to found out digit in sring and lsit
        count = count + 1

print("digit is :", count)
