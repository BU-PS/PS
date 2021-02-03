import math


def solution(w: int, h: int) -> int:
    gcd = math.gcd(w, h)

    all_square = w * h
    broke_square = (w // gcd) + (h // gcd) - 1
    broke_count = gcd

    return all_square - (broke_square * broke_count)


solution(8, 12)