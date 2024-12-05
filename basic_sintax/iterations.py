# for loop

oddNumbers = [1,3,5,7,11,13,17,21,35,43]
for number in oddNumbers:
    print(number);

# printing in a single row
for n in oddNumbers:
    print(n, end = "|")

print("\n");

for n in oddNumbers:
    print(n, end = " ")

print("\nloops using while")
i=0
while i <=15:
    print(i, end = " ")
    i =i+1

print("\n")
j=20
while j>0:
    if(j>2):    
        print(j, end = ", ")
    else:
        print(j, end = "")
    j-=2;

print("\neven numbers")
x =0
while x<=30:
    if(x%2==0):
        print(x, end = " ")
    x+=1      