'''
lv1. 과일 장수
'''
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if i+m <= len(score):
            answer += (min(score[i:i+m]) * m)
    return answer


k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))