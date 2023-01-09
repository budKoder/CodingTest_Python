'''
lv1. 콜라 문제
'''
def solution(a, b, n):
    answer = 0
    while n >= a:
        reget = (n // a) * b
        answer += reget
        n = n % a + (n // a) * b
    return answer



a = 3
b = 1
n = 20
print(solution(a, b, n))