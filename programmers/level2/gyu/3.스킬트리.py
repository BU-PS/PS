def solution(skill, skill_trees):
    count = 0
    
    for trees in skill_trees:
        # 유저 스킬에서 스킬데이터만 가져오기
        skill_data = ''
        for user_skill in trees:
            if user_skill in skill:
                skill_data += user_skill
        
        # 스킬트리가 유효한지 체크
        if skill_data == skill[:len(skill_data)]:
            count += 1

    return count
