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
    left_start, right_end = 0, len(list)-1
    while left_start < right_end:
        while list[left_start] != '.':
            left_start += 1
        while list[right_end] == '.':
            right_end -= 1
        if left_start < right_end:
            list[left_start] = list[right_end]
            list[right_end] = '.'
    return list
new_map = move_blocks(map)

def get_sum(map):
    a = 0
    for idx, num in enumerate(map):
        if num != '.':
            a += idx * int(num)
    return a
    
print(get_sum(map))