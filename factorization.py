#/usr/bin/env python3
import sys


def primef(num):
    if num <= 3:
        return int(num)
    if num % 2 == 0:
        return 2
    elif num % 3 == 0:
        return 3
    else:
        for i in range(5, int(num**0.5) + 1, 6):
            if num % i == 0:
                return int(i)
            if num % (i + 2) == 0:
                return primef(num/(i+2))
    return int(num)


print(primef(int(sys.argv[1])))
