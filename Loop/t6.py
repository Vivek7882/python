#write a program to convert all negative values into positive values in the same list 


list=[12, -45, 7, -3, 89, -22, 0, 34, -9, 56]
print("old list",list)

for item in list:
    if item<0:
        list[list.index(item)]=item*-1



print("new list:",list)