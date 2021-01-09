def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * (n + 1)        # 학생들은 모두 체육복이 있음 
    students[0] = 0                 # (0 번째 무시)
    
    # 잃어버린 거 처리
    for i in lost:
        students[i] -= 1
    
    # 여유분 처리
    for i in reserve:
        students[i] += 1
    
    # 체육복 최대한으로 빌려 줌    
    for i in range(1, n+1):
        if i == 1:                  # 첫번째는 바로 뒤만 빌려줌
            if students[i] == 2 and students[i+1] == 0:
                students[i+1] += 1
                
        elif i == n:                # 마지막은 바로 앞에만 빌려줌
            if students[i] == 2 and students[i-1] == 0:
                students[i-1] += 1
                
        else:   # 중간에 있는 학생은 앞, 뒤 빌려줌,
            if students[i-1] == 0 and students[i] == 2:
                students[i-1] = 1
                continue
            if students[i+1] == 0 and students[i] == 2:
                students[i+1] = 1
                

    students = [1 if data >= 1 else 0 for data in students ]    # 1개 이상은 1로, 그렇지 않으면 0
    return sum(students)