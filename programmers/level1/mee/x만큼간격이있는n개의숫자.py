def solution(x, n):
    answer=[]
    zero=[0 for i in range(n)]
    if x>0:
        for i in range(x,x*n+1,x):
            answer.append(int(i))
    elif x==0:
        return zero
    else:
        for i in range(x,(x*n)-1,x):
            answer.append(int(i))
    return answer