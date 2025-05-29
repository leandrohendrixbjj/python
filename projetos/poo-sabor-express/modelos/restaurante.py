class Resturante:
  nome = None
  categoria = None
  situacao = False


res = Resturante()
res.nome = "Pizzaria do João"
res.categoria = "Pizzaria"
res.situacao = True

# Exibindo os métodos e atributos do objeto
print(dir(res))  

# Exibindo os atributos do objeto
print(vars(res))