def solution(n):
    answer = [i for i in str(n)]
    answer.sort(reverse=True)
    return int(''.join(map(str, answer)))


def solution2(n):
    sort_n = sorted(str(n), reverse=True)
    return int(''.join(sort_n))