# Pega os valores na Horizontal

from helper.clear import *
clear()

"""
  0 => 1,4,7
  1 => 3,6,9
  2 => 2,5,8  
"""
value = 2

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for row in range(len(data)):
    col = 0 if value == 0 else len(data) - value
    print(data[row][col])