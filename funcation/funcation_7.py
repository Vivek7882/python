#default argument function
# write a program that will return total inches of given meter, foot, inches 


def getinches (meter,inches=0,foot=0):
    print(f"meter={meter} inches={inches} foot={foot}")

    totalinches=meter*39.3701
    totalinches=totalinches+(foot*12)+inches

    return totalinches

print(getinches(10,20,50))
print(getinches(10,20))
print(getinches(10))
