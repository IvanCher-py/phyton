from itertools import islice
from itertools import count
from itertools import cycle
from sys import argv

script_name, a, b, text_param = argv
a = int(a)
b = int(b)
my_list = [i for i in islice(count(), a, b)]
print(my_list)
my_iter = cycle(text_param)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
