import numpy as np
import pandas as pd

df = pd.read_csv('inputs/input_day_2.txt', sep='\s+', header=None)

def check_row(row):
    values = row.dropna().values
    decreasing = all(x > y for x, y in zip(values, values[1:]))
    increasing = all(x < y for x, y in zip(values, values[1:]))
    monotonicity = 1 if increasing or decreasing else 0
    is_dif = 1 if all(y - 3 <= x <= y + 3 and x != y for x, y in zip(values, values[1:])) else 0
    return monotonicity * is_dif
        
df['is_dif1'] = df.apply(check_row, axis=1)
print(df['is_dif1'].sum())