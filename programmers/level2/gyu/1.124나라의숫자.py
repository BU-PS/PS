def solution(n):
    answer = ''
    
    while n:
        n, mod = divmod(n, 3)
        
        if mod == 0:
            answer += '4'
            n -= 1
        else:
            answer += str(mod)
            
    return answer[::-1]