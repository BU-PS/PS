# 두 리스트의 길이 = 1 차이
# 정렬, 정렬
# 다른 값 찾기


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]