#1    -8   27  -64  .....    1000

number=1
cube=0

while cube<1000:
    cube=number*number*number
    

    if number%2==0:
        cube=0-cube

    print(cube,end=" ")
    number=number+1


    
    