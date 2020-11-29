def solution(s, n):
    s = list(s) 
    
    for i in range(len(s)):                                     
        if s[i].isupper():                                  # 대문자면, 'A' 만큼 빼고 + n % 26(알파벳수) 함. (A 에서 몇개 더 추가해야하는지 판단)
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
        elif s[i].islower():                                # 소문자면, 'a' 만큼 빼고 + n % 26(알파벳수) 함. (A 에서 몇개 더 추가해야하는지 판단)
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
            
    return "".join(s)