def solution(s):
    answer = sorted(s, reverse=True)
    c="".join(answer)
    return c