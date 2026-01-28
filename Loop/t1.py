#write a program to count odd and even number in numeric list

list=[1,2,3,4,5,6,7,8,9]
count=0
count1=0

for item in list:
    if item%2==0:
        count=count+1
    else:
        count1=count1+1

print("even number is",count)
print("odd number is",count1)