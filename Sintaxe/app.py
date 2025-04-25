from itertools import islice

from helper.limpa_tela import *
clear()

limit = 2
data = {
    1: "Alice",
    2: "Bruno",
    3: "Carla",
    4: "Daniel"
}

for nome in islice(data.items(),limit):
    print(nome)




