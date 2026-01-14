#write a program to findout whether particular key/value exist in dictionary or not using in operator

insert=input("enter value:")

word={'name':"vivek","age":20,"city":"bhavnagar","pincode":364001}
# dictionary is ord only in key not value
found=insert in word

print(found)