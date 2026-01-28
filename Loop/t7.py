# write a program to findout coutries whose area is greater given area.
#  use chatgpt to create dictionaries which country name as key and its' area as value. 


country_area = {
    "India": 3287263,
    "United States": 9833517,
    "China": 9596961,
    "Russia": 17098242,
    "Canada": 9984670,
    "Brazil": 8515767,
    "Australia": 7692024,
    "Argentina": 2780400,
    "Kazakhstan": 2724900,
    "Algeria": 2381741
}

area=int(input("enter area:"))


for item in country_area:
    if country_area[item]>area:
        print(item,country_area[item])
