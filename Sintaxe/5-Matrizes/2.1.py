# Impressão diagonal esquerda, CURTA: 3,5,7

from helper.clear import clear
clear()

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(data)):
    column = len(data) - 1 - row
    print(data[row][column])