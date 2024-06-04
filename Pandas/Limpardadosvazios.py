import pandas as pd

df = pd.read_csv("dataframewitherrors.csv")

new_df = df.dropna()

print(new_df.to_string())

#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.

#Change the original DataFrame by adding the inplace parameter:
'''import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())


Vai colocar 130 em todos os valores vazios
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)


'''