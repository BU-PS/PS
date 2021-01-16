def solution(dartResult):
    answer = []
    steps = []
    
    # result 를 각 단계로 분리 - 3 단계
    start = 0
    end = 0
    while end < len(dartResult):
        if dartResult[end] in ["#", "*", "S", "D", "T"]:
            steps.append(dartResult[start:end+1])
            end += 1
            start = end
        else:
            end += 1
    
    # step 별로 점수 계산
    for step in steps:
        if len(step) != 1:
            number = int(step[:-1])
            bonus = step[-1]
            if bonus == 'S':
                answer.append(number)
            elif bonus == 'D':
                answer.append(number ** 2)
            elif bonus == 'T':
                answer.append(number ** 3)
        else:
            if step == '*':
                if len(answer) >= 2:                # #4 #6
                    answer[-1] = answer[-1] * 2
                    answer[-2] = answer[-2] * 2
                else:                               # #5
                    answer[-1] = answer[-1] * 2
            elif step == '#':
                answer[-1] = answer[-1] * -1 

    return sum(answer)