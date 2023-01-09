'''
lv1. 숫자 짝궁
'''
from collections import Counter
def solution(X, Y):
    answer = ''
    cx = Counter(X)
    cy = Counter(Y)
    it = {k: min(cx.get(k), cy.get(k)) for k in cx.keys() & cy.keys()}
    if len(it) == 0:
        return "-1"
        
    for k, v in sorted(it.items(), reverse=True):
        answer += k*v
    return "0" if answer[0] == "0" else answer


X = "1000000002"
Y = "20200"
print(solution(X, Y))