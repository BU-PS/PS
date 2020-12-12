# 문제 풀이
# 1. index 값 (작업을 수행한 수)를 지정한다
# 2. 아래 주어 진 조건을 실행한다
# 3. 500 이상이 되는 경우 -1


def solution(n: int):
    index = 0

    while index < 500:
        index += 1

        if n == 1:
            return index

        if n & 1:
            n = (n * 3) + 1

        else:
            n = n // 2
    return -1


solution(6)