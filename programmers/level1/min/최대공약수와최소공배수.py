# 최대 공약수 (GCD) : 두 개 이상의 자연수의 공통인 약수 중 가장 큰 수
# 1. 최대 공약수를 구하는 법
# - 두수의 약수들을 구한다
# - 두수의 약수들을 집합(set)에 넣는다
# - 교집합을 통해 공약수를 찾는다
# - 교집합을 중 가장 큰 수를 찾는다

# 최소 공배수 (LCM) : 두 수의 공배수가 최소인
# 1. 최소 공배수를 구하는 법
# - N * M = L * C 의 식을 통해 값을 구한


def solution(n: int, m: int):
    gcd_value = gcd(n=n, m=m)
    lcm_value = lcm(n=n, m=m, g=gcd_value)
    return [gcd_value, lcm_value]


def gcd(n: int, m: int):
    max_value = max([n, m])
    n_cm = set()
    m_cm = set()

    for i in range(1, max_value + 1):
        if n % i == 0:
            n_cm.add(i)
        if m % i == 0:
            m_cm.add(i)

    return max(n_cm & m_cm)


def lcm(n: int, m: int, g: int):
    return n * m // g


solution(4512, 18)
