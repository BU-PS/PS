def solution(n):
    answer=list(str(n))
    answer.sort()
    answer.reverse()
    return int("".join(answer))