import re
import numpy as np

text = open("inputs/input_day_4.txt", "r").read().splitlines()

text_array = np.array([list(row) for row in text]) 
rows, cols = text_array.shape
mas = r'(?=(MAS|SAM))'
a2 = 0

for row in range(rows-2):
    for col in range(cols-2):
        diagonal_tl_to_br = [text_array[row + i][col + i] for i in range(3)] 
        diagonal_bl_to_tr = [text_array[row + 2 - i][col + i] for i in range(3)]
        x1 = ''.join(diagonal_tl_to_br)
        x2 = ''.join(diagonal_bl_to_tr)
        if re.match(mas, x1) and re.match(mas, x2):
            a2 += 1
print(a2)