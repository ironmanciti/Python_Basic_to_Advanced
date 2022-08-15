# 문제 1
with open('test.txt', "w") as file3:
    data = file3.write("한국소프트웨어 산업협회 훈련과정 :\n 알고리즘으로 배우는 Python")

try:
    f = open('test.txt', 'r')
    text = f.read()
    print(text)
    f.close()
except IOError:
    sys.write("File reading error")
    
#%%
# 문제 2
# 다음 file 을 읽어서 가장 빈번하게 나타나는 top 10 단어들을 출력 
f = open('poet.txt')
counts = dict()

for line in f:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

count_lst = []
for k, v in counts.items():
    count_lst.append((v, k))
        
print(sorted(count_lst, reverse=True)[:10])