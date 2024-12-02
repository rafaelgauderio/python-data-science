int(4+5)
print(4-5)

# division
print(20/5)
print(15/3)
print(16/3)
print(16/5==17/5) # false
print(float(16/5)==16.0/5.0) # true
print(16/5==16.0/5.0) # true

# mod = remeider
print(17%3) # 2

# potentiation
print(8**2) # 64
print(5**3) # 125

# double equality "equals"
print(5==5.0) # true
print(5**3==125) # true
print(5>=3) # true
print(5<=2) # false

# line continuation slash continue the line
print (5 * 3 + \
       2) # 17
# jumping line
print("\n"+ str(5 *3 +2))

# indexing
print("Rafael"[0]) # R
print("Rafael"[4]) # e

# indentation is impornt in python
print("\nindentation")
def plusTwo(x):
    x = x+2
    return x

print(plusTwo(7))
print(plusTwo(10))

def powerToTheThree(y):
    y=y**3
    return print(y)

powerToTheThree(4)

def convertToString(x):
    x = str(x)
    return x

age = 50
print("Idade: " + convertToString(age))