
from helper.clear import clear
clear() 

cabecalho = ["Nome", "Idade", "Profissão"]

dados = [
    ["Alice", "30", "Engenheira"],
    ["Bruno", "25", "Designer"],
    ["Carlos", "28", "Programador"]
]

# Define a largura de cada coluna
larguras = [10, 6, 15]

# Imprime o cabeçalho formatado
linha = ""
for texto, largura in zip(cabecalho, larguras):
    linha += texto.ljust(largura)
print(linha)

# Imprime uma linha separadora
print("-" * sum(larguras))

# Imprime os dados
for linha_dado in dados:
    linha = ""
    for texto, largura in zip(linha_dado, larguras):
        linha += texto.ljust(largura)
    print(linha)
