import time


def decorators_decorator(call_count: int, start_sleep_time: int, border_sleep_time: int, factor: int):
    # Декоратор декоратора, принимающий на вход аргументы:
    # call_count - количество запусков;
    # start_sleep_time - начальное время повтора;
    # border_sleep_time - конечное время повтора;
    # factor - во сколько раз увеличиваем время ожидания.
    def time_decorator(func):  # Декоратор, принимающий на вход функцию.
        def wrapper(*args, **kwargs):
            count = 1
            t = start_sleep_time
            result = func(*args, **kwargs)
            print(f'Ожидаемое количество запусков = {call_count}')
            print('Начало работы')
            print(f'Запуск номер {count}. Ожидание {t} секунд. Результат декорируемой функции = {result}')
            for count in range(2, call_count + 1):  # Запускаем цикл по количеству call_count.
                if t < border_sleep_time:  # Если время ожидания меньше конечного, увеличиваем ожидание.
                    t *= 2 ** factor
                elif t >= border_sleep_time:  # Если время ожидания больше или равно конечному, используем последнее.
                    t = border_sleep_time
                time.sleep(t)  # Ожидаем.
                print(f'Запуск номер {count}. Ожидание {t} секунд. Результат декорируемой функции = {result}')
            print('Конец работы')
            return

        return wrapper

    return time_decorator


@decorators_decorator(3, 1, 100, 1)
def func(n, m):
    return n*m


func(2, 3)
