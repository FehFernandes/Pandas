import pandas as pd 

#pd.options.display.max_rows = 99999999999

df = pd.read_json("data.json")

print(df.info())