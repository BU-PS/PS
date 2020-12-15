# 1. 숫자 split -> 해당 수 더하기 = x
# 2. 입력받은 수를 x 로 나누기
# 3. 나누어 떨어지면 true 아니면 false


def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0