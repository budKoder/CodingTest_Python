'''
lv1. 옹알이(2)
'''
def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for idx, val in enumerate(possible):
            if val in b:
                b = b.replace(val, str(idx+1))
        b = "0" + b        
        for i in range(1, len(b)):
            if not b[i].isdigit() or b[i] == b[i-1]:
                break
        else:
            answer += 1
    return answer

babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))