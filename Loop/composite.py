# write a program to figure out whether given number  is composite number or not

n = int(input("Enter a number: "))
count = 0
i = 1

while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1

if n > 1 and count > 2:
    print("Composite number")
else:
    print("Not a composite number")

