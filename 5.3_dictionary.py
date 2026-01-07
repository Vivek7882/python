person = {'name':'vivek solnaki','age':19,'weight':58.22,'gender':True,'isMarried':False}

print(person['name'])

print(person.get('age'))

print(person.get('dob'))

person2=person.copy()
print(person,person2)

person2.clear()
print(person2)

print(person.keys())# show key of the dictinary
print(person.values())# show values of the dictinary

print(person.items())# show all the item of the dictinary

book=['name','price','author','pages']
python_book=dict.fromkeys(book)

python_book['name']='python'
python_book['price']=100
python_book['author']='vivek'
python_book['pages']=200

print(python_book)

python_book.pop('pages')
python_book.popitem()
python_book.pop('country',False)
print(python_book)