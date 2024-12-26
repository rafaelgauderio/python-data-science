# representative (realistic) models require multiple regressions
# y = inferred value, bo = intercept, b1*x = coefficient 8 independent variable
# after 3 dimensions, we do not a visual way to represent the data

# Adjusted R-squared smaller R²
# adjusted r-squared measueres how your model fits the data, but penalizes excessive use of variables
# Adjusted R-squared is the vases for comparing models
# A parameter that increases R-squared but decreases adjusted R-squared holds no predictive power, so can be omitted

import numpy as np
import seaborn 
import pandas as pd
import matplotlib.pyplot as pyplot
import statsmodels.api as stat
seaborn.set()

data = pd.read_csv('multiple_linear_regression.csv');
print(data)

# describe statistics
data.describe()
x = data[['SAT','RANDOM']]
y = data['GPA']
x = stat.add_constant(x)
final_results = stat.OLS(y,x).fit()
print(final_results.summary());

# F-statistics follows an F-distributin
# The lower ther F-statictc, the closer is to a non-significant model