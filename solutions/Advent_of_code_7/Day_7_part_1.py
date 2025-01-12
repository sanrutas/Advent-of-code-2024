from tqdm import tqdm 
from itertools import product

input = open("inputs/input_day_7.txt", "r").read().splitlines()

goals = [int(row.split(':')[0]) for row in input if ':' in row and row]
numbers = [[int(num) for num in row.split(':')[1].split()] for row in input if ':' in row and row]

def update(symbol, eq, new_num):
    if symbol == '+':
        eq += new_num
    if symbol == '*':
        eq *= new_num
    if symbol == '|':
        eq = int(f"{eq}{new_num}")
    return eq

def check_sym(combos, numbers, goal):    
    for combo in combos:
        eq = numbers[0] 
        for num in range(1, len(numbers)):  
            eq = update(combo[num-1], eq, numbers[num])
        if eq == goal:
            return True

sym = ['+', '*']
correct = 0
for num in tqdm(range(len(goals))):
    num_row = numbers[num]
    goal = goals[num]
    combos = product(sym, repeat=len(num_row)-1)
    if check_sym(combos, num_row, goal):
        correct += goal
print(correct)