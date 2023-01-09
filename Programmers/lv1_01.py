'''
lv1. 개인정보 수집 유효기간
'''
def solution(today, terms, privacies):
    answer = []
    for idx, p in enumerate(privacies):
        sDate, dType = p.split()
        month = 0
        for t in terms:
            if dType == t[0]:
                month = int(t.split()[-1])
                break
        y, m, d = map(int, sDate.split("."))
        m += month
        d -= 1
        if d <= 0:
            m -= 1
            d += 28
        while m > 12:
            y += 1
            m -= 12
        y = str(y)
        m, d = map(lambda x:str(x).zfill(2), [m, d])
        if int(today.replace(".","")) > int("{}{}{}".format(y, m, d)):
            answer.append(idx+1)
    return answer


if __name__ == "__main__":
    today = "2022.02.28"
    terms = ["A 23"]
    privacies = ["2020.01.28 A"]
    print(solution(today, terms, privacies))