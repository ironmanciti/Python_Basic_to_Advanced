lorem = """
대법원장은 국회의 동의를 얻어 대통령이 임명한다. 헌법재판소는 법률에 저촉되지 아니하는 범위안에서 심판에 관한 절차, 내부규율과 사무처리에 관한 규칙을 제정할 수 있다. 감사원은 원장을 포함한 5인 이상 11인 이하의 감사위원으로 구성한다. 의무교육은 무상으로 한다. 언론·출판에 대한 허가나 검열과 집회·결사에 대한 허가는 인정되지 아니한다.

국군은 국가의 안전보장과 국토방위의 신성한 의무를 수행함을 사명으로 하며, 그 정치적 중립성은 준수된다. 헌법재판소는 법관의 자격을 가진 9인의 재판관으로 구성하며, 재판관은 대통령이 임명한다. 국무총리는 국회의 동의를 얻어 대통령이 임명한다. 모든 국민은 종교의 자유를 가진다. 국방상 또는 국민경제상 긴절한 필요로 인하여 법률이 정하는 경우를 제외하고는, 사영기업을 국유 또는 공유로 이전하거나 그 경영을 통제 또는 관리할 수 없다.
"""
word_list = lorem.split()
word_list.sort()

def findword(word):
    start = 0
    end = len(word_list)
    words = word_list
    search_count = 0

    while(start < end):
        search_count += 1
        middle = len(words) // 2
        
        if words[middle] == word:
            return search_count
        elif words[middle] > word:
            start, end = 0, middle
        else:
            start, end = middle + 1, len(words)
            
        words = words[start:end]

print(findword('헌법재판소는'))
#%%
max_count = 0
for word in word_list:
    count = findword(word)
    if count > max_count:
        max_count = count

print("max_count = ", max_count)
#%%
total_search_count = 0
for word in word_list:
    count = findword(word)
    total_search_count += count
    
average_cnt = total_search_count / len(word_list)

print('average_cnt = {:.2f}'.format(average_cnt))

