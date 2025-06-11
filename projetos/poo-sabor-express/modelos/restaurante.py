class Resturante:

  data = []

  def __init__(self,nome, categoria):
    self.nome = nome 
    self.categoria = categoria
    self._ativo = False
    Resturante.data.append(self)

  def __str__(self):
    return f'{self.nome} - {self.categoria} - {self._ativo}'  
  
  def list():
    print(f'{"Nome":<25} {"Categoria":<25} {"Situação":<5}')
    for data in Resturante.data:
      print(f'{data.nome.ljust(25)} {data.categoria.ljust(25)} {data._ativo}')  

  """
  Property: sinaliza ao desenvolvedor (ou a si mesmo no futuro) que esse atributo:
    1- Não deve ser acessado diretamente fora da classe
    2- Pode estar sujeito a mudança
    3- Pode ter lógica especial envolvida no acesso (como uma propriedade @property depois)  
  """
  @property
  def ativo(self):
    return "True" if self._ativo else "False"

res = Resturante('Pizzaria do João', 'Pizzaria')
res_1 = Resturante('Churrascaria do Zé', 'Churrascaria')

Resturante.list()

#print(res.__str__())  


# Exibindo os atributos do objeto
#print(vars(res))

# Exibindo os métodos e atributos do objeto
#print(dir(res))  
