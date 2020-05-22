import json
import random

filename = "username.json"
#программа именно чтения данных
with open(filename) as file:
    data = json.load(file)
    data = data[random.randint(0,2)]
    print(f"Welcome back, {data['username']}")
    print(f"Ваш рост сегодня {data['height']}")

