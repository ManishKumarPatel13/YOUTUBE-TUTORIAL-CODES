# Pandas Series
import pandas as pd 

data = pd.read_csv('weather.csv',sep=',')
# print(data)

# part two of our pandas series

# print(data.head(8))
# print(data.tail(6))
# print(data.dtypes)
# print(data.info())
# print(data.columns)
# print(len(data.columns))


# part three of our pandas series

# print(data.describe())
# print(data.describe(include='object'))
# print(data['Evaporation'].describe())

# part four of our pandas series
# x = data[['Evaporation','Rainfall']]
# print(x)


y = data.iloc[9,4]
print(y)