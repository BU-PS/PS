def solution(n):
    check = [1 for i in range(n+1)]
    
    for i in range(2, n+1):                     # 파이썬은 n+1 해야 n까지 반복
        if check[i] == 1:
            for j in range(i*2, n+1, i):
                check[j] = 0

    return sum(check)-2                         # 0과 1 제외