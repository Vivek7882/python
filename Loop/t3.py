#write a program to count words in given string 

s = input("Enter a string: ")
words = s.split()#  .split is use to breaks the string into words using spaces.
count = 0

for item in words:
    print(words)
    count = count + 1

print("Number of words:", count)

