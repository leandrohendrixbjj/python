# ljust() em Python é usado com strings e alinha o texto à esquerda

from helper.clear import clear

clear()

nome = "João"
print(nome.ljust(10))       # 'João      '
print(nome.ljust(10, '-'))  # 'João------'

