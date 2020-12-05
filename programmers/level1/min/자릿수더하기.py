def solution1(n):
    n = str(n)
    return sum([int(i) for i in n])


def solution2(n):
    return sum([i for i in list(map(int, str(n)))])


def solution(n: int):
    return eval("+".join(list(str(n))))