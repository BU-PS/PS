# new_id의 len은  3이상 15이하
# new_id는 모두 소문자이어야함.
# new_id는 -,_,.만 사용가능한데 .은 처음과 끝은 사용할 수 없고 연속적으로 사용할 수 없음.
# 새로 알게된 부분
    # import re
    # re.sub(r'제거하고싶지않은부분','제거하고싶은부분을 어떻게 바꿀것인가',변수명) 
    # re.sub('제거하고싶은부분','그 부분을 어떻게 바꿀것인가',변수명)
    # startswith와 endswith를 이용하면 시작부분과 끝부분에 문자를 찾을 수 있음.
import re
def solution(new_id):
    # 1단계
    answer=new_id.lower()
    # 2단계
    answer=re.sub(r'[^a-z0-9\-\_\.]','',answer)
    # 3단계
    answer=re.sub('[..]+','.',answer)
    # 4단계
    if answer.startswith('.'):
        answer=answer[1:]
    if answer.endswith('.'):
        answer=answer[:-1]
    # 5단계
    if len(answer)==0:
        answer+="a"
    # 6단계
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    # 7단계
    while len(answer)<=2:
        answer+=answer[-1]
        
    return answer