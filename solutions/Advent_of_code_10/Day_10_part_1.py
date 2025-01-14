input = open("inputs/input_day_10.txt", "r").read().split()

def in_bounds(row, col):
    if 0 <= row < len(input) and 0 <= col < len(input[0]):
        return True

def check_nearby(input, tocheck, curr_num=0, offsets = None):
    if offsets is None:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
    
    neighbours = set()
    
    for row, col in tocheck:
        for ox, oy in offsets:
            new_row, new_col = row + ox, col + oy
            if in_bounds(new_row, new_col) and int(input[new_row][new_col]) == curr_num + 1:
                neighbours.add((new_row, new_col))
    if curr_num < 8:
        return check_nearby(input, neighbours, curr_num + 1)
    else:
        return len(neighbours)

def get_sum(input):
    sum = 0
    for row_id, row_num in enumerate(input):
        for col_id, col_num in enumerate(input[row_id]):
            if col_num == '0':
                sum += check_nearby(input, [(row_id, col_id)])
    return sum

print(get_sum(input))