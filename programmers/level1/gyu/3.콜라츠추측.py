def solution(num):
    LIMIT = 501
    count = 0
    
    for _ in range(LIMIT):
        if num == 1:
            return count
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        count += 1
    
    return -1