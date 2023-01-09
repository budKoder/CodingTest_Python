'''
lv1. 명예의 전당(1)
'''
def solution(k, score):
    answer = []
    top = []
    for i in range(len(score)):
        top.append(score[i])
        top.sort(reverse=True)
        top = top[:k]
        answer.append(top[-1])
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))