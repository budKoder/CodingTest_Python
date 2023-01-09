'''
lv1. 푸드 파이트 대회
'''
def solution(food):
    answer = ''
    for idx, val in enumerate(food):
        answer += str(idx) * (val//2)
    answer += '0'
    answer += answer[len(answer)-2::-1] 
    return answer

food = [1, 7, 1, 2]
print(solution(food))