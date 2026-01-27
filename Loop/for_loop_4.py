#for loop with string
# count vowels  

name=input("enter your name:")
vowel=['a','e','i','o','u']
count=0

for item in name:
    if str.lower(item) in vowel:# str.lower is conver upper case into lower case
     count=count+1
    # print(item)

print(count)