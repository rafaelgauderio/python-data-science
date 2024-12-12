import numpy as np;
import pandas as pd;
import matplotlib.pyplot as pt
import statsmodels.api as st

data = pd.read_csv('linear_regression_price_weight.csv');

print(data);

y = data['price']
x = data['weight']
k0=st.add_constant(x);
results = st.OLS(y,k0).fit();
print(results.summary());

pt.scatter(x,y);
yRegression = 102200 + 222.9402*x;
figure = pt.plot(x,yRegression, lw=2, c='orange', label='regression line')
pt.xlabel('PRICE', fontsize=19)
pt.ylabel('WEIGHT', fontsize=19)
pt.xlim(200);
pt.ylim(100000);
pt.show();
