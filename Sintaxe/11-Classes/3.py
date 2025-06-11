# Property in Classe 
from helper import clear
clear.clear()

class Pessoa:
  def __init__(self, name,age):
    self.name = name
    self.age = age   
    self._active = True

"""
  Property: sinaliza ao desenvolvedor (ou a si mesmo no futuro) que esse atributo:
    1- Não deve ser acessado diretamente fora da classe
    2- Pode estar sujeito a mudança
    3- Pode ter lógica especial envolvida no acesso (como uma propriedade @property depois)  
"""
@property
def active(self):
  return 'True' if self._active else 'False'   
  
pessoa = Pessoa('leandro',40)

print(vars(pessoa))