def solution(arr: list, divisor: int):
    answer = []
    for ar in sorted(arr):
        if not (ar % divisor):
            answer.append(ar)

    return answer if len(answer) else [-1]