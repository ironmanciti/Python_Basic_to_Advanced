def gcd(m, n):
    if m < n:
        print('큰수를 먼저 입력해 주세요')
        return
    while m % n != 0:
        m, n = n, m % n
    return n

print(gcd(44, 12))