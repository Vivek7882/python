number=input("enter number:")

number=int(number)

print(number)
last=number%10
first=number//10

print(last)
print(first)

word=['zero','one','two','three','four','five','six','seven','eight','nine']


print(word[first],' ',word[last])