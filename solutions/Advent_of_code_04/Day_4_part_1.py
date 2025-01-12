import re
import numpy as np

text = open("inputs/input_day_4.txt", "r").read().splitlines()

text_array = np.array([list(row) for row in text]) 
rows, cols = text_array.shape
xmas = r'(?=(XMAS|SAMX))'
a = 0

for row in text:
    a += len(re.findall(xmas, row)) 

for col in range(cols):
    vertical_string = ''.join(text_array[:, col])  
    a += len(re.findall(xmas, vertical_string))  

for offset in range(-rows + 1, cols):
    start_row = max(0, offset)
    start_col = max(0, -offset)
    diagonal_length = min(rows - start_row, cols - start_col)  
    diagonal_characters = [text_array[start_row + i][start_col + i] for i in range(diagonal_length)]  
    diagonal_tl_to_rb = ''.join(diagonal_characters) 
    a += len(re.findall(xmas, diagonal_tl_to_rb))

for offset in range(rows + cols - 1):  
    start_row = max(0, offset - cols + 1)  
    start_col = min(cols - 1, offset)  
    diagonal_length = min(start_col + 1, rows - start_row)  
    diagonal_characters = [text_array[start_row + i][start_col - i] for i in range(diagonal_length)]  
    diagonal_tr_to_lb = ''.join(diagonal_characters)  
    a += len(re.findall(xmas, diagonal_tr_to_lb))  

print(a)