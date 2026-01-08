set1={1,2,3,4,5}
set2={4,5,6,7,8,}

print(set1,set2)

set3=set1.union(set2)

print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set1.difference(set2)
print(set5)

number={1,2,3,4,5,6,89,5,4,3,4,5,544,65,65,46,65,1,3,4,3,}

print(len(number))

# remove all the duplicat value
u_number=set(number)
print(number)   