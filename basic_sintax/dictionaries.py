# disctionaries represents a data sctructure
# key, value - like a map from Java
# use curly braces {}

dic01 = {'k1':'bette','k2':'chayote','k3':'radish','k4':'lettuce'}
print(dic01)
print(dic01['k1'])
print(dic01['k4'])

# change a value
dic01['k4']='arugula'
dic01['k5']='cucumber'
print(dic01)

# departments
dep_works= {'TI':'Rafael','RH':['Larrisa','Ana','Mary']}
print(dep_works['TI'])
# the second element are a list
print(dep_works['RH'])

print("Empty dictionary")
Professors = {}
Professors['Drama'] = 'Angela'
Professors['Comedy'] = 'Yasmin'
Professors['Action'] = 'Tom'
Professors['Documentary']=None
print(Professors)
print(Professors['Drama'])
print(Professors.get('Drama'));
print(Professors.get('Epic'));

# examplçe
Menu = {'meal_1':'Beef', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}

Price_list = {}
Price_list['Beef']=10
Price_list['Fries']=20
Price_list['Cheeseburger']=12
Price_list['Lasagna']=35
Price_list['Soup']=7.5
print(Price_list)
