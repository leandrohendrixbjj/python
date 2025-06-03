class Resturante:

  data = []

  def __init__(self,nome, categoria, situacao):
    self.nome = nome 
    self.categoria = categoria
    self.situacao = situacao
    Resturante.data.append(self)

  def __str__(self):
    return f'{self.nome} - {self.categoria} - {self.situacao}'  
  
  def list():
    for data in Resturante.data:
      print(f'{data.nome} - {data.categoria} - {data.situacao}')

  

res = Resturante('Pizzaria do João', 'Pizzaria', 'Aberto')
res_1 = Resturante('Churrascaria do Zé', 'Churrascaria', 'Fechado')

Resturante.list()

#print(res.__str__())  


# Exibindo os atributos do objeto
#print(vars(res))

# Exibindo os métodos e atributos do objeto
#print(dir(res))  
