# just if
x = 10
y = 50
if x > 3 and y > 13:
    print('Both conditions are correct')
if x <= 3 or y <= 13:
    print('At least one of the conditions is false')


# elif
x = 115

if x > 200: 
    print ("Big")
elif x > 100 and x <= 200:
    print ("Average")
elif x <= 100 and x >= 0:
    print("Small")
else:
    print("Negative")


# using def
def compareAge(age):
    if(age < 0):
        return "Can not inform negative age!"
    elif age>=0 and age<18:
        return "Minor"
    elif age>=18 and age <65:
        return "Of legal age"
    else:
        return "Elderly"

print(compareAge(-10))
print(compareAge(3))
print(compareAge(21))
print(compareAge(79))
print(compareAge(0))

# indentation
def evenOrOdd(number): 
   if str(number).replace('.','',1).isdigit()==False:
       print(str(number) + " is not numeric value")   
   else:
       number = float(number)
       if number%2==0:
           print(str(number) + " is even!")
       else:
           print(str(number) + " is odd")
           
evenOrOdd('Rafael')
evenOrOdd(17)
evenOrOdd(12)
evenOrOdd(3.15)
evenOrOdd(True)