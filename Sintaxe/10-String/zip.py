# ZIP: Percorre coleções simultaneamente, emparelhando elementos com base nas suas posições.
from helper.clear import clear
clear

nomes = ['Lucas', 'Ana', 'João']
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")