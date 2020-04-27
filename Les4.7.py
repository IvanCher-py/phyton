from math import factorial
from itertools import islice
from itertools import count


def fact(n):
    a = [i for i in islice(count(1), n)]
    for j in a:
        yield factorial(j)


n = int(input('Укажите число до которого необходимо расчитать факторил: '))
for el in fact(n):
    print(el, end=' ')