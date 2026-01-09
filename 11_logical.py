n1=int(input('enter number n1:'))
n2=int(input('enter number n2:'))
n3=int(input('enter number n3:'))

result=n1<n2 and n2<n3
print(f"{result}={n1<n2}and{n2<n3}")

result=n1>n2 and n2<n3
print(f"{result}={n1>n2}and{n2<n3}")

result=n1<n2 or n2<n3
print(f"{result}={n1<n2}or{n2<n3}")

result=n1>n2 or n2<n3
print(f"{result}={n1>n2}ro{n2<n3}")

result=n1>n2 or n2>n3
print(f"{result}={n1>n2}or{n2>n3}")








