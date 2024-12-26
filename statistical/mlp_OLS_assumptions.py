# Assumptions for regression analysis (5 Assumptions)
# 1. Linearity
    # A straight line fits the data well
    # We can easy transform appropriately the regression when the relationship between the data is not linear
# 2. No endogeneity
    # ommitted variable bias (we forget to include a relevant variable on our model)
    # ommited variable bias (ovb) is hard to fix
    # This omitted variable reflects in the error term as the factor we forgot to include in our model
# 3. Normality and homoscedasticity
    # if the mean os not expected to be zero, the linear model is not the best fitting one, but just having and intercept solves this problem
    # Homoscedasticity means to have equal variance
    # To prevents heteroscedasticity we can check for ovb, lool for outliers and use a log transformation (semi-log model)
# 4. No autocorrelation
    # Is observerd in time series data
    # Errors are assumed to be uncorrelated, is the relalated we have a problem
    # No serial correlation
    # Is is not observerd in a cross-sectional data
# 5. No multicollinearity
    # Easy to notice and easy to fix, but it is a big problem
    # Occurs when 2 or more variables have a high correlation
    # We can fix dropping one of the 2 variables, transform them to 1 variable or keep both variables
    # To prevent we have to find the correlation between each 2 pairs of independent variables