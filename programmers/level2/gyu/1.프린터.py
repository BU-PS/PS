def solution(priorities, location):
    answer = 0
    priorities = [(priority, idx)for idx, priority in enumerate(priorities) ]    

    while True:
        if max(priorities)[0] == priorities[0][0]:      # 가장 큰 값 찾기
            answer += 1
            if priorities[0][1] == location:            # 내가 찾고자 하는 경우인지
                break
            else:
                priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))        # 가장 큰 값 아니면 맨 뒤로 보내기 

    return answer