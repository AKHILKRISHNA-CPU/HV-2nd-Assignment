import pandas as pd
# Created two Pandas series
FirstSeries = pd.Series([10,15,20,25,30,35])
SecondSeries = pd.Series([2,4,6,8,10,12])
# Performing arithmetic operations on the two series
addition = FirstSeries + SecondSeries
subtraction = FirstSeries - SecondSeries
multiplication = FirstSeries * SecondSeries
division = FirstSeries / SecondSeries
modulus = FirstSeries % SecondSeries
# Printing the results of the arithmetic operations
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulus)


