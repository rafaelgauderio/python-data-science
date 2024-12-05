# itirations with dictionaries with the same key and different values
prices = {
    "i5 processor" : 500.50,
    "ram memory" : 230.20,
    "hard disk" : 300.42
}    

quantity = {
    "i5 processor" : 1,
    "ram memory" : 4,
    "hard disk" : 2
}

## because the keys are the same can iterate with dictionary prices or quantity
def calc_total(price,quant):
    total=0.0;
    for i in price:
        total+= price[i] * quant[i]
    return "R$ "+ str(format(total, ".2f"));

def calc_total_quantity(price,quant):
    total=0.0;
    for i in quant:
        total+= price[i] * quant[i]
    return "R$ "+ str(format(total, ".2f"));

print(calc_total(prices,quantity));
print(calc_total_quantity(prices,quantity));

prices02 = {
    "spaghetti" : 6,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity02 = {
    "spaghetti" : 6,
    "lasagna"  :  7,
    "hamburger" : 1
    }

money_spent = 0

for item in prices02:
    if(prices02[item]>=5):
        money_spent= money_spent + (prices02[item] * quantity02[item]);
    
print(money_spent);