import numpy as np
import statistics
input = open("inputs/input_day_5.txt", "r").read().splitlines()

rules = [[int(x) for x in row.split('|')]for row in input if '|' in row and row]
updates = [[int(x) for x in row.split(',')] for row in input if '|' not in row and row]

filtered_sets = {}
for update in updates:
    relevant_rules = []
    for rule in rules:
        if all(num in update for num in rule):
            relevant_rules.append(rule)
    filtered_sets.update({tuple(update): relevant_rules})

def rule_checker(update, rules):
    level = {}
    for num in update:
        level[num] = 0
    for rule in rules:
        if rule[1] in level: 
            level[rule[1]] +=1
    seq = []
    for num in update:
        seq.append(level[num])
    if all(x <= y for x, y in zip(seq, seq[1:])):
        return update
    else: 
        sorted_update = sorted(level, key=level.get)
        return sorted_update
        
bad_sum = 0
for update in updates:
    result = rule_checker(update, filtered_sets[tuple(update)])
    if result != update:
        bad_sum += result[len(result)//2]
print(bad_sum)