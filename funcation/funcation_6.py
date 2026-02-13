

def getresult (*value): #  * means tuple
    count=0
    total=0
    for item in value:
        count =count+1
        total=total+item
        avg=total/count

    print(f"count= {count} total= {total} avg= {avg}")

getresult(1,2,45,48,4448)