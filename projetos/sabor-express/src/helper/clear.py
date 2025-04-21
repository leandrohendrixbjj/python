import os

def clear():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)
