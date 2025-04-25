import bcrypt

# Senha que você quer hashear
senha = "121212"

# Gerando o salt
salt = bcrypt.gensalt(rounds=12)  # rounds=12 é o fator de custo

# Gerando o hash bcrypt
hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)

print(hashed)
