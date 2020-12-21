def solution(n):
    #수정
    x=n**(1/2)
    return (x+1)**2 if x%1==0 else -1
    
    # x=n**(1/2)
    # if x%1==0:
        # return (x+1)**2
    # return -1