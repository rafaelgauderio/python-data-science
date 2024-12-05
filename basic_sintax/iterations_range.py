# Loops with List
# range(start, stop, step)
# start include, stop exclude
print(range(0,15,1))
print(list(range(0,15,1)))

# include 1 and exclude 21
print(list(range(1,21,2)))

# include 30 and exlcude -1 (30 to zero)
print(list(range(30,-1,-2)))

# Use the range() function to create a list with all numbers from 0 to 19
print(list(range(0,20,1)));

print("conditional and range\n")
for i in range(5,21,1):
    if(i%2==0):
        print(i, end = " even, ")
    else:
        print(i, end = " odd, ")

print("\n")
array =['Rafael','Julia','Claudia','Zara']
for item in range(len(array)):
    print(array[item], end = " ")    

print("\nPrinting the same list with static value on start, stop, step");
for item in range(0,4,1):
    print(array[item], end = " ")    


print("\nCreate a For loop that will print all the variables from a given list multiplied by 2. Let the list contain all numbers from 1 to 20");
double_list=list(range(1,21,1))
for item in range(len(double_list)):
    print(double_list[item] * 2, end = " ")

print("\nprinting string Even and odd numbers")
for item in range(1,30):
    if(item%2==1):
        print(item, end = " ")
    else:
        print("Even", end = " ")

print("\nExercise")
n = [1,2,3,4,5,6,7]
for item in n:
    print(item*3, end =" ")
print("\nAnother solution")
x=0;
while x < 7:
    print(n[x]*3, end = " ");
    x = x + 1;