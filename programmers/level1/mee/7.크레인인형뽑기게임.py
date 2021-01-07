# 0은 다 무시하고 숫자를 뽑기(0이라면 다시 돌아가서 그 다음거 검사)
# 0이 아닌 숫자가 나오면 빈배열에 넣어주고 0만들기
# 숫자를 넣은 배열에 숫자가 겹치면 삭제
# 삭제한숫자가 생기면 카운트세기

def solution(board, moves):
    answer = 0 # 겹쳐서 지운숫자 개수
    kakao=[] # 뽑은 인형(숫자)들을 넣을 배열
    base=[[board[j][i] for j in range(len(board))] for i in range(len(board))] 
    # moves를 하기위한 1,2,3,4,5 게임판 만들기
    
    
    for i in moves:
        for j in range(len(base)):
            if base[i-1][j]==0:
                continue
            kakao.append(base[i-1][j])
            base[i-1][j]=0
            break
                
        if len(kakao) >= 2 and kakao[len(kakao)-1] == kakao[len(kakao)-2]:
            kakao.pop()
            kakao.pop()
            answer+=2
        

    # for k,l in enumerate(kakao):
    #     if kakao[k]==kakao[k-1]:
    #         del kakao[k]
    #         del kakao[k-1]
    #         answer+=2
                        
    return answer