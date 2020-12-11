def uclid(n, m):
    # 유클리드 호제법
    while True:
        mod = m % n 
        if mod == 0:
            return n
        m, n = n, mod
    
def solution(n, m):
    if n > m:
        n, m = m, n
        
    GCD = uclid(n, m)
    LCM = (n // GCD) * (m // GCD) * GCD
    return[GCD, LCM]