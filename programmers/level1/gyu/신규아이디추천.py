def solution(new_id):
    import re
    
    # 1 단계
    new_id = new_id.lower()
    
    # 2 단계 - _ . (특수문자 모두 고려하지 않아서.. 73점 맞음ㅋㅋ)
    new_id = re.sub('[!@#$%^&*()+=/?:${}~<>\[\],]', '', new_id)
    
    # 3 단계 - 모두 특수문자인 경우 new_id 가 없음.
    if(new_id): 
        temp = ''
        for i in range(len(new_id)-1):
            if new_id[i] == '.' and new_id[i+1] =='.':
                pass
            else:
                temp += new_id[i]
        new_id = temp + new_id[-1] # 마지막 문자 추가해줘야함.
        
    # 4 단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5 단계
    if not new_id:
        new_id = 'a'
    
    # 6 단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7 단계
    if len(new_id) <= 2:
        for i in range(len(new_id), 3):
            new_id += new_id[-1]
    
    return new_id