import random
from timeit import Timer

from questions import get_biggest_and_lowest_value


if __name__ == '__main__':
    numbers = []
    for _ in range(1000000):
        numbers.append(random.uniform(1, 100))

    t = Timer(lambda: get_biggest_and_lowest_value(numbers))
    print(t.timeit(number=1))

