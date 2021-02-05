# 선행스킬순서(skill)에서 나올 수 있는 경우의 수 표현하기.
# skill_trees 원소들을 나열해 skill과 겹치는 스킬순서를 더해서 경우의 수와 비교해서 +1 해주기.
# 제출후 채점에서 4개만 맞는다. 왜그럴까? 이유를 알았다 아예 들어있지 않은 경우가 있다.
def solution(skill, skill_trees):
    answer=0
    skill_pass = [skill[0:i+1] for i in range(len(skill))] # 가능한 경우의 수 
    
    for i in skill_trees:
        arr =""
        for j in i:
            if j in skill:
                arr += j
        if arr in skill_pass or len(arr)==0:
            answer += 1
    return answer