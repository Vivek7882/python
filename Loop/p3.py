# write a program to print given amount into words
# input : 12345 output : one two three four five 

word=['zero','one','two','three','four','five','six','seven','eight','nine']

list=[]
number=int(input("enter number:"))

while number>0:
    reminder=number%10
    list.insert(0,word[reminder])
    number=number//10

print(" ".join(list))

