# Mean = the average value (the sum of all values divided by number of values).
# Median = the value in the middle, after you have sorted all values ascending.
# Mode = the value that appears most frequently.

import pandas as pd

df = pd.read_csv("dataframewitherrors.csv")

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

'''import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)



import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0
'''