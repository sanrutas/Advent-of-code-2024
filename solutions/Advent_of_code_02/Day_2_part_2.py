import numpy as np
import pandas as pd

df = pd.read_csv('inputs/input_day_2.txt', sep='\s+', header=None)
def check_row2(row):
    values = row.dropna().values
    decreasing = all(x > y for x, y in zip(values, values[1:]))
    increasing = all(x < y for x, y in zip(values, values[1:]))
    monotonicity = 1 if increasing or decreasing else 0
    is_dif = 1 if all(y - 3 <= x <= y + 3 and x != y for x, y in zip(values, values[1:])) else 0
    if monotonicity * is_dif == 1:
        return 1
    
    for i in range(len(values)):
        modified_values = np.delete(values, i)
        decreasing = all(x > y for x, y in zip(modified_values, modified_values[1:]))
        increasing = all(x < y for x, y in zip(modified_values, modified_values[1:]))
        monotonicity = 1 if (increasing or decreasing) else 0
        is_dif = 1 if all(abs(y - x) <= 3 and abs(y - x) >= 1 for x, y in zip(modified_values, modified_values[1:])) else 0
        if monotonicity * is_dif == 1:
            return 1
    return 0
    
df['is_dif2'] = df.iloc[:,0:8].apply(check_row2, axis=1)

print(df['is_dif2'].sum())