# O desempacotamento com ** (para dicionários) e * (para listas/tuplas) é um recurso muito útil 

data = {"nome": "Maria", "idade": 30}
complement = {"cidade": "São Paulo"}

# Unindo os dois dicionários:
info = {**data, **complement}
print(info) # {'nome': 'Maria', 'idade': 30, 'cidade': 'São Paulo'}
