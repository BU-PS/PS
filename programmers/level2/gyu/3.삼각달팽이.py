def solution(n):
    triangle = [[0] * n for _ in range(n)]
    
    # triange 만들기
    number = 1
    # x가 -1 로 시작하는 이유는 아래로 증가해야할때 마지막에 인덱스를 넘어가기 때문에 -1 로 시작하고 증가시킨 다음에 데이터를 삽입하는 방법 사용
    x, y = -1, 0
    for i in range(n):
        for j in range(n-i):
            if i % 3 == 0:
                # 아래로 이동
                x += 1
            if i % 3 == 1:
                # 오른쪽으로 이동
                y += 1
            if i % 3 == 2:
                # 왼위로 이동
                x -= 1
                y -= 1
            triangle[x][y] = number
            number += 1
    
    # triangle 에서 1차원 배열로 변환
    answer = []
    for column in triangle:
        for data in column:
            if data:
                answer.append(data)
            
    return answer