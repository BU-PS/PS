def solution(num):
    answer=0
    while True:
        if num%2==0:
            num=num/2
            answer+=1
            continue
        elif num==1 or answer==500:
            break
        else:
            num=num*3+1
            answer+=1
            continue
    if answer>=500:
        return -1
    return answer