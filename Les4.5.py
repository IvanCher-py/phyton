from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


a = [int(i) for i in range(100, 1001)]
print(a)
print('\nПроизведения всех элементов списка', reduce(my_func, a))
