input = open("inputs/input_day_9.txt", "r").read().strip()

def get_map(input):
    map = []
    for id, num in enumerate(input):
        if id % 2 != 0:
            for i in range(int(num)):
                map.append('.')
        else:
            for i in range(int(num)):
                map.append(str(id//2))
    return map
    
map = get_map(input)

def move_blocks(list):
    list = list[:]
    max_len = len(list) - 1
    left_start, right_end = 0, max_len
    while 0 <= right_end:
        
        # finds the position of a number that has not yet been checked on the right (right_end), then finds how many times it repeats to the left and assigns right_start
        while list[right_end] == '.':
            right_end -= 1
        right_start = right_end
        while list[right_start] == list[right_start-1]:
            right_start -= 1
        
        # finds position of the first number on the left (left_start), that is not bigger than first_right position
        while list[left_start] != '.' and left_start < right_start:
            left_start += 1
        
        # if free space is not to the left of the current right number, then reset left_start and move to the next number 
        if left_start >= right_start:
            right_end = right_start-1
            left_start = 0
            continue 
        
        # finds current free space block end position (left_end)
        left_end = left_start
        while list[left_end] == list[left_end+1] and left_end < max_len:
            left_end += 1
        
        # If numbers fit, move them, reset left_start and move to the next right number cycle
        len_left = len(range(left_start, left_end)) + 1
        len_right = len(range(right_start, right_end)) +1 
        if len_left >= len_right:
            for id in range(0, len_right):
                list[left_start+id] = list[right_end-id]
                list[right_end-id] = '.'
            left_start = 0
        # if numbers don't fit, look for the next block of space to the right
        else:
            left_start += len(range(left_start, left_end)) + 1
        
    return list

new_map = move_blocks(map)
def get_sum(map):
    a = 0
    for idx, num in enumerate(map):
        if num != '.':
            a += idx * int(num)
    return a
    
print(get_sum(new_map))