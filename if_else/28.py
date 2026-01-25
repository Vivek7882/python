d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

if m < 3:
    m += 12
    y -= 1

k = y % 100
print(k)
j = y // 100
print(j)

h = (d + (13*(m+1))//5 + k + k//4 + j//4 + 5*j) % 7

if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wednesday")
elif h == 5:
    print("Thursday")
else:
    print("Friday")
