def cash_decorator(func):
    # Декоратор, принимающий на вход функцию.
    d = {}  # Словарь, в котором хранятся пары 'входные данные - результат работы функции'.

    def wrapper(*args):
        if args in d.keys():
            return d[args]  # Если входные данные есть в словаре, возвращаем зачение, не запуская функцию.
        else:
            result = func(*args)
            print('Func worked')  # Если входных данных нет в словаре, то запускаем функцию.
            d[args] = result  # Записываем получившуюся пару в словарь.
            return result

    return wrapper


@cash_decorator
def multiplier(number: int):
    return number * 2


print(multiplier(3))
print(multiplier(5))
print(multiplier(3))
print(multiplier(5))
print(multiplier(3))
