"""
1) 다음 프로그램의 결과값은 ?
"""
xlist = []
xlist.append('Good')
xlist.append('Morning')
print(xlist)

xlist.append([3, 4])
print(xlist)

"""
2) 다음 list 의 element 를 오름차순으로 정렬 (ascending sort) 한다.
또한, 내림차순 (descending order)으로 정렬한다.
sort(), sort(reverse=True) 함수를 사용한다.
"""
xlist = [2, 1, 3, 5, 4]

print(sorted(xlist))
print(sorted(xlist, reverse=True))

"""
3) 두개의 list element 들을 짝을 지워 출력
"""
stocks = ['삼성전자', '대한항공', 'google', 'apple']
close = [40000, 2000, 50000, 100000]

for s, c in zip(stocks, close):
    print(s, c)
