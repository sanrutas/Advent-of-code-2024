import re 

text = open("inputs/input_day_3.txt", "r").read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, text)
sum = 0
for x, y in matches:
    sum += int(x)*int(y)
print(sum)