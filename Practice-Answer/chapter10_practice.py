"""
1) parameter 로 받은 string 의 양 끝단 2 글자를 붙여서 반환하는 함수
"""
def both_ends(s):
    if len(s) < 2:
        return ''
    first2 = s[:2]
    last2 = s[-2:]
    return first2 + last2

print(both_ends('spring'))
print(both_ends('Hello'))

#%%
"""
2) 두개의 문자열을 parameter 로 받아 서로의 첫번째 두 글자를 교환한 후 중간에 한칸 띄우고 반환하는 함수
"""
def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

print(mix_up('frog', 'dinner'))
#%%

"""
3) 두개의 parameter 를 받아서 두개가 같으면 SAME 다르면 Different 를 반환하는 함수
"""
def test(got, expected):
    if got == expected:
        print('SAME')
    else:
        print('Different')

test('a', 'a')
test('aba', 'aca')

"""
4) 다음의 string에서 slicing을 이용하여 `500`이라는 문자열을 출력하라.
"""
stock_index = "SP500"
print(stock_index[2:]
