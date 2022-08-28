import re
import numpy as np
from random import randint as rand
from math import floor
large_numbers = np.floor(np.linspace(range(20, 61, 20)[rand(0, 2)], 100, num = 4))
#print(large_numbers)
no_of_large_numbers = len(large_numbers)
select_large_numbers = int(input('How many large numbers do you want:  '))
small_numbers = np.array([[x,x] for x in np.arange(1, 11, 1)])
small_numbers = small_numbers.flatten()
#print(small_numbers)
pos = rand(0,13)
number_set = np.append(large_numbers[0:select_large_numbers],small_numbers[pos:(pos + (6 - select_large_numbers))])
print(number_set)
bracket_pos = rand(0, 1)
bracket1 = ['', '(']
bracket2 = ['', ')']
operators = ['+', '*']
operators2 = ['+', '/', '*']
number_set = np.char.mod('%d', number_set)
target = bracket1[bracket_pos] + bracket1[bracket_pos] + number_set[0] + operators2[rand(0,2)] + number_set[1] + operators[rand(0,1)] + number_set[2] + bracket2[bracket_pos] + operators2[rand(0,1)] + number_set[0] + operators[rand(0,1)] + number_set[3] + operators[rand(0,1)] + number_set[4] + bracket2[bracket_pos] + operators[rand(0,1)] + number_set[5]
print(number_set)
print(target)
print(eval(target))


regex = r'[0-9]+'
string = '(7+7)/22'
result = eval(string)
found = re.findall(regex, string)
if (found):
    print(found, result)
else:
    print(found, result)
