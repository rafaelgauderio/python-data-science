# liner regression is a linear approximation of causal relationship between two or mode variables
# simple linear regression
# y = Ko + K1.x1 + Error

# Correlation: relantionshio between to variables, movement together, f(x,y)=f(y,x), single point graphic
# regression: one variable affects the other, cause and effect, of(x,y) != f(y,x), graphic is a line

import numpy
import pandas
import matplotlib.pyplot as plot
import statsmodels.api

# load data from file
dataFrame = pandas.read_csv('simple_linear_regression.csv');
print(dataFrame)

print(dataFrame.describe());

# create a regression
# define the dependent variable as y and independent as x
y = dataFrame['GPA']
x = dataFrame['SAT']

# plot the data
matplotlib.pyplot.scatter(x,y)
plot.xlabel('SAT', fontsize=15);
plot.ylabel('GPA', fontsize=16);
plot.show();

# OLS regression results

x0= statsmodels.api.add_constant(x);
results = statsmodels.api.OLS(y,x0).fit();
print(results.summary());

# basing on OLS results plot the regression line
plot.scatter(x,y);
yReg = 0.275 + 0.0017*x ;
figure = plot.plot(x,yReg, lw=4, c='red', label = "regression line")
plot.xlabel('SAT', fontsize = 15);
plot.ylabel('GPA', fontsize = 15);
plot.show();