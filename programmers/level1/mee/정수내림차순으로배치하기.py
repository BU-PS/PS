def solution(n):
    #수정
    answer=list(str(n))
    return int(''.join(sorted(answer,reverse=False)))

    
    # answer=list(str(n))
    # answer.sort()
    # answer.reverse()
    # return int("".join(answer))