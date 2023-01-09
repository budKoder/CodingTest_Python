'''
lv1. 기사단원의 무기
'''
def getDivCnt(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return len(d)


def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        cnt = getDivCnt(n)
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer


number = 10
limit = 3
power = 2
print(solution(number, limit, power))