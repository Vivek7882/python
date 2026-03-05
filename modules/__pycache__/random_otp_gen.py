import random as r

count=1
digit=[]


while count<=4:
    
    digit.append(str(r.randint(0,9)))
    count=count+1

digit=''.join(digit)#conver list into string
print(digit)


print("ganrate opt of four digit:",r.randrange(1000,9999))