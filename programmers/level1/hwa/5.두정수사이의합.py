def solution(a, b):
    answer=0
    
    if a>b:
        for c in range(b,a+1):
            answer=answer+c
        
    elif b>a:
        for c in range(a,b+1):
            answer=answer+c
    
    elif a==b:
        answer =a
    
    return answer