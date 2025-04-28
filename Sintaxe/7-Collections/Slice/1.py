# slice => fatiar, quando você quer uma parte de um objeto, com list
from itertools import islice

limit = 3
data = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']

# Pegando os 3 primeiros
for nome in islice(data, limit):
    print(nome)
