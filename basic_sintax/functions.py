# def fucntion_name (parameters):
#    function_body

# void function
def printName(name):
    print(name)

myName='Rafael de Luca'
printName("My name is " + myName)

# function with return parameter
import math
def squareRoot(x):
    y = float(math.sqrt(x))
    return y
print(squareRoot(81))

def powerOfThree(y):
    return y**3;
x = powerOfThree(6);
print(x);

def exponentiation_exp_2(x):
    result = x**2
    print("Raised to the power of 2:")
    return result    
exponentiation_exp_2(17.5)


print("Fuction within a function")
def payment(working_hours):
    return working_hours * 9;
def payment_with_extra(w_hours):
    return payment(w_hours) * 1.2;

def plus_five(args):
    y = args + 5
    return y
def m_by_3(x):
    return plus_five(x) * 3 
print(m_by_3(5))

print(payment(10))
print(payment_with_extra(10))

def triangle(a,b,c):
    if a==b and b==c:
        return "equilateral triangle"
    elif (a==b and b!=c) or (a!=b and b==c) or (a==c and b!=c):
        return "isosceles triangle"
    else: 
        return "scalene triangle"

print(triangle(2,2,2))
print(triangle(1,3,3))
print(triangle(4,4,1))
print(triangle(5,2,5))
print(triangle(1,3,7))


print("\nBuilt-in Funcions")

print(type(17))
print(type(17.12))
print(type('Rafael'))
print(int(3.1415))
print(float(17))
print(str(50.13))

maximum =  max(17,12,82,31)
print(maximum)
print(min(17,12,82,31))
print(abs(-34))

number = float(3.1585)
formatted_number = "{:.3f}".format(number)
print(formatted_number)

import math
rounded_up = math.ceil(number)
print(rounded_up)

power_ten = pow(2,10)
print(power_ten)

print("Array function")
import numpy
array = [1,2,4,8,16,32,64,128]
print(sum(array))
print(len(array))
array_float = [3.15,5.22,7.83]
print(numpy.ceil(array_float))

def distance_from_zero(x):
    if type(x)==int or type(x)==float:
        print(abs(x))
    else:
        print("Not possible with string")

distance_from_zero(-20)
distance_from_zero("Rafael")
distance_from_zero(-3.1415)

def round_half_up(n):
    if n - int(n) == 0.5:
        return int(n) + 1
    else: 
        return int(n)
# Example usage
print(round_half_up(3.5))
print(round_half_up(2.2))
