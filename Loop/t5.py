#write a program to count vowels, consonants, digits, words, and symbol in given list

#data = ['a', 'B', 'e', 'k', '1', '9', '@', '#', 'Hello', 'Python', 'i', 'Z', '5', '$']
data=input("enter strin:")
vowel=['a','e','i','o','u']
consonants =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
digit=[1,2,3,4,5,6,7,8,9,0]
v=0
c=0
d=0
s=0

for item in data:
    if item in vowel:
        v+=1
    elif str.lower(item) in consonants:
        c+=1
    elif item in digit:
        d=+1
    else:
        s+=1


print("vowel is:",v)
print("consonants is:",c)
print("digit is:",d)
print("symbol is:",s)
print("Total words are : ",len(data.split()))