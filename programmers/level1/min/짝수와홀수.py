# 짝수인 경우 Even 홀수인 경우 Odd
# 1. 짝수 홀수 판별
# 2. 리턴


def solution(num: int):
    return "Even" if num % 2 == 0 else "Odd"


def solution1(num: int):
    return "Odd" if num & 1 else "Even"
