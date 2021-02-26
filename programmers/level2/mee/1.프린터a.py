def solution(priorities,location):
    answer=0
    priorities=[(j,i) for i,j in enumerate(priorities)]

    while True:
        if max(priorities)[0]==priorities[0][0]:
            answer+=1
            if priorities[0][1]==location:
                break
            else:
                priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))

    return answer