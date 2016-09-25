data="1000,ChenghaoQ,Male"
Mydict={}
#Using data split
(Mydict['HP'],Mydict['name'],Mydict['sex'])=data.split(',')

print("HP:    "+Mydict['HP'])
print("Name:  "+Mydict['name'])
print("Sex:   "+Mydict['sex'])
