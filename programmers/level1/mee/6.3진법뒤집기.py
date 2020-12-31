#(1)10진법을 3진법으로바꾸기
    # while문으로 3으로 나누었을때 몫이 0이 될때가지 계산
    # 나온 나머지값을 넣기
    # 마지막 몫도 넣기
#(2)바꾼 3진법 뒤집기
    # reverse로 값뒤집기(3단계 계산을 위해)
#(3)뒤집은 3진법을 10진법으로 만들어 리턴
    #3^n으로 계산

def solution(n):
    answer=0
    re=[]
    
    while n>=3:
        re.append(n%3)
        n=n//3
    re.append(n)
    re.reverse()

    for i in range(len(re)):
        answer+=re[i]*(3**i)

    return answer