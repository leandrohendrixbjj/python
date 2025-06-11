# Property in Classe 
from helper import clear
clear.clear()

class Pessoa:
  def __init__(self, name,age):
    self.name = name.title()
    self.age = age    

  """
    classmethod recebe a classe como primeiro argumento, em vez da instância
     1-) Por convenção, chamamos esse primeiro parâmetro de cls (assim como usamos self para instâncias).
     2-) Ele pode ser usado para acessar ou modificar atributos da classe, ou para criar instâncias alternativas.

    Quando usar:
      1-) Precisa acessar ou modificar atributos da classe
      2-) Quer criar instâncias alternativas (como fábricas)
      3-) Quer um método que não dependa de uma instância específica 
  """   
  @classmethod
  def criar_bebe(cls,nome):
    return cls(nome,0)
 
adulto = Pessoa('leandro',40)
print(vars(adulto))

bebe = Pessoa.criar_bebe('Luna')
print(vars(bebe))

