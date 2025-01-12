import pandas as pd
with open("inputs/input_day_1.txt", 'r') as textfile:
    input = textfile.read().splitlines()

df = pd.DataFrame([line.split() for line in input], columns=['Column1', 'Column2']).astype(int)
for col in df:
    df[col] = df[col].sort_values(ignore_index=True)
df['Absolute_Difference'] = (df['Column1'] - df['Column2']).abs()
print(df['Absolute_Difference'].sum())
