import re 

text = open("inputs/input_day_3.txt", "r").read()

do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"
collect = True
sum2 = 0
for x in re.finditer(f'{do}|{dont}|{mul}', text):
    if re.fullmatch(do, x.group()):
        collect = True
    elif re.fullmatch(dont, x.group()):
        collect = False
    elif collect:
        sum2 += int(x.group(1)) * int(x.group(2))
print(sum2)