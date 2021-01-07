# lost와 reserve 서로 중복되는 숫자 빼주기
# reserve i-1 i+1가 lost와 같으면 lost에서 없애주기
# n-len(lost) return
def solution(n,lost,reserve):
    lost_a=[i for i in lost if i not in reserve]
    reserve_a=[i for i in reserve if i not in lost]

#if i+1을 먼저 했더니 테스트11번에서 실패해 뭐가 잘못되었나 한참동안 고민함..
    for i in reserve_a:
        if i-1 in lost_a:
            lost_a.remove(i-1)
        elif i+1 in lost_a:
            lost_a.remove(i+1)
    
    return n-len(lost_a)
