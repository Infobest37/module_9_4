
from pprint import pprint
file_name = 'test.txt'
strings = [   'Text for tell.',

              'Используйте кодировку utf-8.',
              'Because there are 2 languages!',
              'Спасибо!'
              ]

def custom_write(file_name, strings):
    strings_positions = {} # cоздаем словарь куда будем помещать все наши  действия
    file = open(file_name, 'a', encoding='utf-8') #Открываем нужный нам файл
    line_number = 1 # Создаем мифическую линию которой будем говорит потом что это наша строка
    for string in strings: # Прогоняем все наши строки через цикл
        tell_1 = file.tell() # считаем курсор
        file.write(f'{string}\n') # записываем нашу строку в файл через интер
        strings_positions[line_number] = tell_1, string # strings_positions[line_number] тут мы говорим что
        # [line_number] это наш ключ который будет считать строки и после сравниваем их с положением с курсором и самой строкой которую считаем
        line_number += 1 # создаем счетчик для каждой строки если строка добавляется она увеличивает ее на 1
    pprint(strings_positions) # выводим на экран то что у нас получилось согласно файла








result = custom_write(file_name, strings)