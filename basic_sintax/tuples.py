# tupples are a type of data sequences that are IMMUTABLE, can not append or delete elements
# use parentheses, are the default sequence type 
ages = (17,15,20,18,37)
names = 'Rafael','Angela','Zara','Clara','Zoe'
print(ages)
print(ages[0])
print(ages[-1])

print("Join list and tupples")
List_join = [names,ages]
Tupple_join = (names,ages)
print(List_join)
print(type(List_join))
print(Tupple_join)
print(type(Tupple_join))
list02 = (name,age) = ('Rafael de Luca#35').split('#')
print(list02)
print(name)
print(age)

a,b,c = 'Hello','World','User'
print(a)
print(b)
print(c)

print("Funcions with tupples")
def square_mesuares(side):
    a = side**2
    p = 4*side
    print("The side, area and perimeter of the square are: ")
    return side,a,p
square_mesuares(5)
