'''
lv1. 문자열 나누기
'''
def solution(s):
    answer = 0
    while s:
        for i in range(len(s)):
            cnt = s[:i+1].count(s[0])
            if cnt == i+1-cnt:
                answer += 1
                s = s[i+1:]
                break
        else:
            answer += 1
            break
    return answer


s = "aaabbaccccabba"
print(solution(s))