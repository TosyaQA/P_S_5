#Создайте функцию генератор чисел Фибоначчи

count = int(input('Введите требуемое количество чисел Фибоначчи: '))

def fib(count):
    a, b = 0, 1
    for n in range(count):
        yield a
        a, b = b, a + b

print(list(fib(count)))