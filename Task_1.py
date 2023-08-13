#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

#Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

import os

def parse_path(str):
    path, ext = os.path.splitext(str)
    dirpath, filename = os.path.split(path)
    return (dirpath + "/", filename, ext)

print(
    parse_path("c:/Users/Vladislav/Desktop/deep_to_python/test.txt")
) # ('c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')