'''
lv1. 햄버거 만들기
'''
def solution(ingredient):
    answer = 0
    st = []
    for i in ingredient:
        st.append(i)
        if len(st) >= 4:
            if st[-4:] == [1,2,3,1]:
                for _ in range(4):
                    st.pop()
                answer += 1
    return answer

ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))