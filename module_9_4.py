import random
from pprint import pprint
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
#
# my_list = map(lambda x,y: x == y, first, second)
# print(list(my_list))

def  get_advanced_writer(file_name):
    with open(file_name, "w", encoding='utf-8'):
     def write_everything(*data_set):

        with open(file_name, "w", encoding='utf-8') as f:
            for file in data_set: # для того чтоб создать список не кортежем мы делаем цикл через поступивший файл и
                # прогоняем полученные данные и уже читаем сам файл по строчно а именно то что в нем находится через отступы
                  f.write(f"{file}\n")
            return f
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)



first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())