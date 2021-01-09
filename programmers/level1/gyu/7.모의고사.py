def solution(answers):
    player1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]   
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = []
    count = [0] * 4
    
    # 정답 체크     
    for i, data in enumerate(answers):
        mod_i_1 = i % 10
        mod_i_2 = i % 8
        if player1[mod_i_1] == data:
            count[1] += 1
        if player3[mod_i_1] == data:
            count[3] += 1    
        if player2[mod_i_2] == data:
            count[2] += 1
    
    # 가장 많이 맞힌 학생 찾기       
    _max = max(count)
    for i in range(1, len(count)):
        if count[i] == _max:
            answer.append(i)
    
    return answer