# every value in python is a objet
# Integer, Float, String, Lists
# Object allow the programer to model real-world concepts
# Object = Data + Manipulation Operations
# Class = define the relus for creating a object
# Object (Instance) has atributes (properties) and methods (special function)
# Function: can have many parameters, exists on its on, fucntion()
# Method: the object is one of its parameters, belong to a specific class, object.method()

# a module: pre-written code that has classes, funtions
# a modele can be updated, improved and reused 
# a package (library) is a collection or directory that related to many modules
# the standard library is a collection of modules available when you install Python

import math as m;
import numpy as np;
from math import sqrt as raizQuadrada
from numpy import *

square81 = math.sqrt(81);
print(square81);
print(m.pow(2,10)); 

print(raizQuadrada(121))
print(np.power([1,4,7,9],2))

print("The value of euler´s number is " + str(math.exp(1)));