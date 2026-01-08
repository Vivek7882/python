#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

number=input("enter number:")

number=int(number)
temp=number



first=temp//100  #123 first number 1
temp=temp//10  #123 output 12
mid=temp%10  #12 ouptup 2
last=number%10 # 123 output 3

print(first)
print(mid)
print(last)


word=['zero','one','two','three','four','five','six','seven','eight','nine']


print(word[first],' ',word[mid],' ' ,word[last])