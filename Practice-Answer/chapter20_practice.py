"""
(문제1)
tuple element 로 구성된 list 에서 tuple 의 첫번째 element 가  'a' 인 tuple 이
alist 의 몇번째  element 인지 구하라. 단, for loop 과 비교문을 사용하지 않고 list comprehension 을 사용
"""
# alist = [('x', 4), ('s', 5), ('a', 4), ('t', 5), ('k', 4), ('w', 5), ('a', 4)]

# print([idx for idx, tup in enumerate(alist) if tup[0] == 'a'])

"""
(문제 2)
다음 file 을 읽어서 가장 빈번하게 나타나는 top 10 단어들을 list comprehension 을 이용하여 출력
"""
f = open('poet.txt')
counts = dict()

for line in f:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

print(sorted([(v, k) for (k, v) in counts.items()], reverse=True)[:10])
