# comparison
print("Comparison Operators")
print(27 < 30) # true
print(5*3 <= 5**3) # true
print(100==10**2) # true
print(1712!=1712) # false

#logical operators
print("\nLogical Operators")
print("not precedes and precedes or")
x = (False or True and not False)
print(x) # true
print(True and True) # true
print(True and False) # false
print(True or True) # true
print(True or False) # true
print(False or False) # false
print(True and not False and not False) # true

print("\nWhen copy a Object is Equal but not Identical")
print("because they use different memory addresses")
a = [2,4,8,16]
b = a.copy()
print(a)
print(b)
print(a==b) # true
# using identity operator
print(a is b) # false
print(id(a))
print(id(b))