# write a program to print following series 
# 1     -4      9     -16     25      -36     1000
# 1     2       3       4       5       6  

#squer of the number

number=1
squ=0

while squ<961:
    squ=number*number

    if number%2==0:
        squ=0-squ

    print(squ,end=" ")
    number=number+1