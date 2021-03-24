# 123/1234 => 3 1234 
# 12/34  => 3 2 34  
# 34 => 3 2 3 4

# 41772/52841 => 7 7252841
# 725/2841 => 7 7 2841
# 25/841 => 7 7 5 841

def solution(number,k):
    answer=[]

    for i in number:
        while len(answer)>0 and i>answer[-1]:
            if k>0:
                answer.pop()
                k-=1
            else:
                break
        answer.append(i)

    if k>0:  # 숫자가 중복될 경우도 꼭 생각해주기. ex)11111
        for i in range(k):
            answer.pop()

    return "".join(answer)