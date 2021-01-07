# 1번,2번,3번학생들이 찍는방법 나열
# 1번문제부터 마지막문제까지 각각의 학생들 찍는 방식과 대입
# 가장 많이 맞춘 학생 return

def solution(answers):
    answer=[0,0,0] # s1,s2,s3 각각 맞춘 수 더해주기
    math_s=[] # 가장 많이 맞춘 학생을 담기위한 배열
    s1=[1,2,3,4,5]
    s2=[2,1,2,3,2,4,2,5]
    s3=[3,3,1,1,2,2,4,4,5,5]


# answers도 저 5가지답이 계속 반복될거라 생각해 그렇게 풀었다가 시간이 오래걸렸다. 문제를 더 잘 이해하면서 풀자..
    for i in range(len(answers)):
        if s1[i%5]==answers[i]:
            answer[0]+=1
        if s2[i%8]==answers[i]:
            answer[1]+=1
        if s3[i%10]==answers[i]:
            answer[2]+=1

    for j in range(3):
        if answer[j]==max(answer):
            math_s.append(j+1)
    return math_s



