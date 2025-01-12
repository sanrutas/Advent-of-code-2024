from tqdm import tqdm
input = open("inputs/input_day_6.txt", "r").read().splitlines()

map = [list(r) for r in input]
            
for r in range(len(map)):
    if '^' in map[r]:
        col = map[r].index('^')
        row = r
        break
input_row, input_col = row, col

def collect_locations(map, directions, row, col):
    pos = 0
    checked = [(row, col)]
    map[row][col] = '.'
    while True:
        new_row, new_col = row + directions[pos][0], col + directions[pos][1]
        if not (0 <= new_row < len(map)) or not (0 <= new_col < len(map[0])):
            return checked        
        if map[new_row][new_col] == '.':
            if (new_row, new_col) not in checked:
                checked.append((new_row, new_col))
            row = new_row
            col = new_col
        elif map[new_row][new_col] == '#':
            pos = (pos + 1) % 4
            
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
coords = collect_locations(map, directions, row, col)

def count_loop(map, path_row, path_col, directions):
    map[path_row][path_col] = '#'
    row, col = input_row, input_col
    states = set()
    pos = 0
    while True:
        if (row, col, pos) in states:
            map[path_row][path_col] = '.'
            return True
        else:
            states.add((row, col, pos))
        new_row, new_col = row + directions[pos][0], col + directions[pos][1]
        if not (0 <= new_row < len(map)) or not (0 <= new_col < len(map[0])):
            map[path_row][path_col] = '.'
            break
        if map[new_row][new_col] == '.':
            row = new_row
            col = new_col
        elif map[new_row][new_col] == '#':
            pos = (pos + 1) % 4
count = 0
coords = set(coords[1:])
for row, col in tqdm(coords):
    if count_loop(map, row, col, directions):
        count += 1
print(f'Part 2:', count)