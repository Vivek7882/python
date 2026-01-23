'''
write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21-April 19
    Taurus: April 20-May 20
    Gemini: May 21-June 21
    Cancer: June 22-July 22
    Leo: July 23-August 22
    Virgo: August 23-September 22
    Libra: September 23-October 22
    Scorpio: October 24-November 21
    Sagittarius: November 22-December 21
    Capricorn: December 22-January 19
    Aquarius: January 20-February 18
    Pisces: February 19-March 20

    write a program display marriage compatibility for male female using birth dates as per below link,  accept birth day and birth month from user as separate input for both male & female. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility
https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg

'''
day=int(input("enter borth day for male 1 to 31 :"))
month=int(input("enter birth month for male 1 to 12:"))

day1=int(input("enter borth day for female 1 to 31 :"))
month1=int(input("enter birth month for female 1 to 12:"))


if (month==3 and day>=21) or (month==4 and day<=19):
    male="aries"

elif(month==4 and day>=20) or (month==5 and day<=20):
    print("TAURUS")
    male="taurus"

elif(month==5 and day>=21) or (month==6 and day<=21):
    print("Gemini")
    male="gemini"

elif(month==6 and day>=22) or (month==7 and day<=22):
    print("Cancer")
    male="cancer"

elif(month==7 and day>=23) or (month==8 and day<=22):
    print("leo")
    male="leo"

elif(month==8 and day>=23) or (month==9 and day<=22):
    print("vigro")
    male="vigro"

elif(month==9 and day>=23) or (month==10 and day<=22):
    print("libra")
    male="libra"

elif(month==10 and day>=24) or (month==11 and day<=21):
    print("scorpio")
    male="scorpio"

elif(month==11 and day>=22) or (month==12 and day<=21):
    print("Sagittarius")
    male="sagittarius"

elif(month==12 and day>=22) or (month==1 and day<=19):
    print("Capricorn")
    male="capricorn"

elif(month==1 and day>=20) or (month==2 and day<=18):
    print("Aquarius")
    male="aquarius"

elif(month==2 and day>=19) or (month==3 and day<=20):
    print("Pisces")
    male="pisces"

else:
    print("invlaid data")


if (month1==3 and day1>=21) or (month1==4 and day1<=19):
    print("ARIES")
    female="aries"

elif(month1==4 and day1>=20) or (month1==5 and day1<=20):
    print("TAURUS")
    female="taurus"

elif(month1==5 and day1>=21) or (month1==6 and day1<=21):
    print("Gemini")
    female="gemini"

elif(month1==6 and day1>=22) or (month1==7 and day1<=22):
    print("Cancer")
    female="cancer"

elif(month1==7 and day1>=23) or (month1==8 and day1<=22):
    print("leo")
    female="leo"

elif(month1==8 and day1>=23) or (month1==9 and day1<=22):
    print("vigro")
    female="vigro"

elif(month1==9 and day1>=23) or (month1==10 and day1<=22):
    print("libra")
    female="libra"


elif(month1==10 and day1>=24) or (month1==11 and day1<=21):
    print("scorpio")
    female="scorpio"

elif(month1==11 and day1>=22) or (month1==12 and day1<=21):
    print("Sagittarius")
    female="sagittarius"

elif(month1==12 and day1>=22) or (month1==1 and day1<=19):
    print("Capricorn")
    female="capricorn"

elif(month1==1 and day1>=20) or (month1==2 and day1<=18):
    print("Aquarius")
    female="aquarius"

elif(month1==2 and day1>=19) or (month1==3 and day1<=20):
    print("Pisces")
    female="pisces"

else:
    print("invlaid data")


if male =="aries":
    if female in['taurus','capri',"cancer",'scorpio']:
        print("not match")

    else:
        print("great match")

elif male =="taurus":
    if female in['aries','sagi',"gimini",'aquarius']:
        print("not match")

    else:
        print("great match")

elif male =="leo":
    if female in['virgo','capri']:
        print("not match")

    else:
        print("great match")

elif male =="sagittarius":
    if female in['taurus','virgo',"capri"]:
        print("not match")

    else:
        print("great match")

elif male =="virgo":
    if female in['aries','sagi',"gimini","libra"]:
        print("not match")

    else:
        print("great match")

elif male =="capricorn":
    if female in['aries','sagi',"gimini","aquarius"]:
        print("not match")

    else:
        print("great match")

elif male =="gimini":
    if female in['taurus','cancer',"scorpio","pisces"]:
        print("not match")

    else:
        print("great match")

elif male =="libra":
    if female in['virgo','capri',"scorpio","cancer"]:
        print("not match")

    else:
        print("great match")

elif male =="aquarius":
    if female in['virgo','capri',"taurus","cancer"]:
        print("not match")

    else:
        print("great match")

elif male =="cancer":
    if female in['aries','gimini',"aquarius","libra"]:
        print("not match")

    else:
        print("great match")

elif male =="cancer":
    if female in['sagi','gimini',"aquarius","libra"]:
        print("not match")

    else:
        print("great match")

elif male =="cancer":
    if female in['gimini',"aquarius","libra"]:
        print("not match")

    else:
        print("great match")
