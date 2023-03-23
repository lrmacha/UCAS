import pandas as pd
import numpy as np

df = pd.read_excel('forR.xlsx')

df = df.replace(0, np.nan)

# OR

# df = df.replace(0, '')

df.to_excel('nozeros.xlsx', index = False)

print (df)