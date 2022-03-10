import os
import random


location = input('Введите путь, где располагается музыка: ')

if os.path.exists(location):
    number_of_mus = len(os.listdir(location))
    for file in os.listdir(location):
        file_name = location + "\\" + file
        os.rename(file_name, str(random.randint(0, number_of_mus)) + '. ' + file)
        print(file)
else:
    print('Такого пути не существует')

print('Музыка разбросана')
