
"""
https://eda-ai-lab.tistory.com/468
"""


# 문자열 w를 u, v로 분리하는 함수
def divide(w):
    # p = Parentheses
    openP = 0
    closeP = 0
    
    # 균형 잡힌 문자열로 분리
    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else:
            closeP += 1
        
        # 균형잡힌 u, v 로 분리
        # w[:i+1] 은 올바른 괄호 (u)
        # w[i+1:] 올바른 괄호 데이터로 이후에도 검사하기 위해 분리 (v)
        if openP == closeP:
            return w[:i+1], w[i+1:]
    
# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def isBalanced(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True
    
def solution(w):    
    # 1
    if not w:
        return ''
    
    # 2
    u, v = divide(w)

    # 3
    if isBalanced(u):
        # 3-1
        # u 는 올바른 괄호 이고, 이후 문자열도 올바른 괄호 만들기 위해 solution 호출
        return u + solution(v)
    # 4
    # 올바르지 않으니깐 올바른 괄호 만들기 위한 작업 수행
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        
        # 4-4
        for p in u[1:-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        # 4-5
        return answer