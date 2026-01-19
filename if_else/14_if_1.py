# write a program to find out whether given shape is square or portrait or landscape using user given length and width 
length=int(input("enter lenght:"))
width=int(input("enter width:"))


if length==width:
    print("shape is square")

if length>width:
    print("shape is portrait")

if length<width:
    print("shape is landscape")
