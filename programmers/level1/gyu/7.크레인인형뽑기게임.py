''' 풀이 과정
1. moves 값들을 -1 씩 해주기 (board 랑 맞춤)
2. move의 위치를 0 ~ depth 까지 읽기
    2.1 0 ~ depth 를 읽으면서 중간에 값이 있으면
        해당 값과 stack[-1] 요소와 비교해서 같으면 pop / answer += 2
        같지 않으면 append
    2.2 값이 없으면 (모두 0인 경우) 무시
'''
'''
def solution(board, moves):
    answer = 0
    
    moves = [move -1 for move in moves]
    depth = len(board)
    stack = [0]          # len(stack) 대비 

    for move in moves:
        data = -1
        i = 0
        
        # data 가져옴
        while i < depth:
            if board[i][move]:
                data = board[i][move]
                board[i][move] = 0
                break
            i += 1
        
        # 데이터가 없으면 다음 move 수행
        if data == -1:
            continue
            
        # 데이터 있으면 stack 마지막 요소와 같으면 삭제 그렇지 않으면 append
        if stack[-1] == data:
            stack.pop()
            answer += 2
        else:
            stack.append(data)
        
    return answer
'''

def get_doll(board, move):
    depth = 0
        
    # doll 가져옴
    while depth < max_depth:
        if board[depth][move]:
            doll = board[depth][move]
            board[depth][move] = 0
            return doll
        depth += 1
        
    return -1

def solution(board, moves):
    global max_depth
    answer = 0
    
    max_depth = len(board)
    moves = [move -1 for move in moves]     # board 랑 맞춤
    stack = [0]                             # len(stack) 대비 

    # 인형 뽑기 시작!
    for move in moves:
        doll = get_doll(board, move)

        # 인형(data)이 없으면 다음 move 수행
        if doll == -1:
            continue
            
        # stack 마지막 요소와 같으면 삭제 그렇지 않으면 append
        if stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)
        
    return answer