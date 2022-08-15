"""
1) 다음 문장 수행 후의 output 은 ?
"""
def sigma(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

sigma(10)

"""
2) xlist = [1, 2, 3, 4] 를 한줄에 출력하고 각 element 의 사이는 '/' 로 구분하라.
"""

xlist = [1, 2, 3, 4]

for n in xlist:
    print(n, end="/")

