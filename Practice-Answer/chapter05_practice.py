"""
1) 선형방정식 (linear equation) y = mx + b 를 함수로 작성한다.
    이때, 기본값(default value)은 m = 1, b = 0 로 한다.
"""
def linear(x, m=1, b=0):
    return m * x + b

print(linear(3, m=2, b=5))

"""
2) 다음 함수가 수행된 후 print 되는 값은 ?
"""
def f(x):
    return x + 1, x * x

x, y = f(3)
print(x, y)

"""
3) 다음 code 가 수행된 이후 z 의 값은 ?
"""
def f1(x, y):
    return (x + 1) / (y - 1)

z = f1(2, 2)
print(z)

def f1(x, y=2):
    return (x + 1) / (y - 1)

z = f1(1)
print(z)

"""
4) 섭씨 온도를 화씨 온도로 변환하는 함수를 작성한다. 변환 공식은 다음과 같다.
"""
def fc_convert(tc):
    return 9 / 5 * tc + 32

print(fc_convert(100))
