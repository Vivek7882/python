#Given two lists, convert them into sets and find common elements

list1=[1,2,3,4,5]
list2=[4,5,6,7,8,]

list1=set(list1)
list2=set(list2)

list3= list1.intersection(list2)

print(list3)