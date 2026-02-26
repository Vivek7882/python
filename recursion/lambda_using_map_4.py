#write a program to convert list that has mixed case countries names into uppercase countries name  using lambda
countries = [
    "iNdIa",
    "uNiTeD sTaTeS",
    "cAnAdA",
    "aUsTrAlIa",
    "gErMaNy",
    "fRaNcE",
    "jApAn"
]


getlow=list(map(lambda c:c.upper(),countries))

print("origanal list",countries)

print("lower case list:",getlow)