from collections import deque

def sdvigRight(step):
    l = [1, 2, 3, 4, 5]
    l = deque(l)
    l.rotate((step)*(-1))
    return l
print(sdvigRight(1))


def sdvigLeft(step):
    l = [1, 2, 3, 4, 5]
    l = deque(l)
    l.rotate(step)
    return l
print(sdvigLeft(1))
