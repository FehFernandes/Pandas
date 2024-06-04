import pandas as pd

df = pd.read_csv('dataframewitherrors.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

#df.dropna(subset=['Date'], inplace = True)