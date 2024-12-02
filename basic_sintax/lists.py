## data structure list
## initial index 0 or -1 (last index)

Professors = ['Rafael','Luciana','Zara','Atena']
print(Professors[0])
print(Professors[1])
print(Professors[2])
print(Professors[-1])
## last element
print(Professors[3]==Professors[-1])

## replace
Professors[2]='Laura'
print(Professors)

del Professors[3]
print(Professors)

## append in the end of the list
Professors.append('Joao')
Professors.append('Larissa')
print(Professors)

## extend 
Professors.extend(['Lucas','Agnaldo',False,'Einstein'])
print(Professors)

# concatenets String and list
print("The first elements is " + Professors[0] + '.')
print("The last elements is " + Professors[-1] + '.')

print("The size of the list is " + str(len(Professors)) + '.')

# slice
# first digit is inclusive, second exclude
# printing 2,3,4 elements 
print(Professors[2:5])

# the fisrt two elements
print(Professors[:2])
# the last two
print(Professors[-2:])

# index of a element
print(Professors.index('Rafael'))

Students = ['Juliana','Claudia']
# list of list
Bigger_List = [Professors, Students]
print(Bigger_List)

# order list
# first have to remove the boolean element, to became a list just of Strings
print(Professors.index(False))
del Professors[7]

Professors.sort()
print(Professors)

Professors.sort(reverse=True)
print(Professors)
