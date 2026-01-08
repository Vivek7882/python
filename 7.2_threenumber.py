number=input('enter number:')
number=int(number)

temp=number

first=temp//100
temp=temp//10
mid=temp%10
last=number%10

print(first,mid,last)

word1=[ 'hunded','one hundred','two hundredr','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
word2=['','','twenty','thirty','fouty','fifthy','sixty','seventy','eighty','ninety']
word3=['zero','one','two','three','four','five','six','seven','eight','nine']

print(word1[first],word2[mid],word3[last])




