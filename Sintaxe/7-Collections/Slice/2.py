# slice => fatiar, quando você quer uma parte de um objeto, com dict
from itertools import islice

limit = 2
data = {
    1: "Alice",
    2: "Bruno",
    3: "Carla",
    4: "Daniel"
}

result = dict(islice(data.items(), limit))

print(result)
