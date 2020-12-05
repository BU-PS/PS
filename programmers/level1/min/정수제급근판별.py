# 1. 루트를 사용
# 2. 루트를 사용했을때 정수값이 떨어지면 입력받은값에 + 1 후 제곱하여 리턴
# 3. 그렇지 않은 경우 -1을 리턴

# Note
# 루트를 사용하는 경우 정수가 나오는것이 아닌 실수형식으로 나옴 !


def solution(n: int) -> int:
    m = n ** 0.5

    if isinstance(m, float) and m % 1 == 0:
        return int((m + 1) ** 2)
    return -1