from typing import Optional
from helper.clear import *

clear()

def getName(name: Optional[str] = None) -> str:
    if name is None:
        return 'Soares'
    return name

data = getName('leandro')
print(data)  # Resultado: leandro

data2 = getName()
print(data2)  # Resultado: Soares
