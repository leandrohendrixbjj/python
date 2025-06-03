from helper.clear import clear
clear()

# Usamos essa função pq Phyton não interpreta == e ===
def loose_comparison(a,b):
    try:
       return float(a) == float(b)
    except (ValueError, ValueError):
        return str(a) == str(b)
        

data = 3
info = '3.0'

if loose_comparison(data, info):
  print('They are equal')
else:
  print('They are not equal')
