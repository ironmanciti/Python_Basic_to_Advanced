"""
1) 다음의 출력 결과는 ?
"""
d = {'a': 2, 'b': 4, 'c': 9}
for x in sorted(d):
    print(d[x], end="")

"""
2) 다음의 출력 결과는 ?
"""
d = {'a': 2, 'b': 4, 'c': 9}
for x in sorted(d.values()):
    print(x, end="")
#%%
"""
3) 다음의 출력 결과는 ?
"""
d = {'a': 21, 'b': 4, 'c': 9}
for x in sorted(d.items()):
    print(x, end="")
#%%
d = {'a': 21, 'b': 4, 'c': 9}
print(sorted(d.items(), key=lambda kv: kv[1]))
#%%
"""
4) dictionary 를 이용하여 자신의 정보를 구조화 하여 작성
"""
personInfo = {
    'name': '오영제',
    '성별': '남성',
    '거주지': {
            '도시': '서울',
            '동': '충무로',
            '주소': '123-45',
            },
    '전화번호': 1012345678,
    '신장': 175.17
}

print(personInfo)
#%%
"""
5) 두개의 주사위를 던져서 두 주사위의 합이 같은 것끼리 출력
"""
import pprint
d = {}

for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        newTuple = (dice1, dice2)
        added = dice1 + dice2
        if added not in d:
            d[added] = []
        d[added].append(newTuple)

pprint.pprint(d)
