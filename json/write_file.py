import json

filename = "username.json"

main_spi = []
while True:
    name = input("Введите ваше имя")
    if name == 'q':
        break
    height = input("Введите ваш рост")
    spi = {'username': name, 'height': height}
    main_spi.append(spi)
with open('username.json', 'w') as file:
    json.dump(main_spi, file)
