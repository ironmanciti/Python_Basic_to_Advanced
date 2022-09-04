def findword(word, words):
    start = 0
    end  = len(words) 
    search_count = 0
    
    while (start < end):
        search_count += 1
        middle = len(words) // 2        # 가운데의 위치
        
        if words[middle] == word:       # found
            return search_count
        elif words[middle] > word:      # 찾으려는 단어가 아래쪽 절반에 위치
            start, end = 0, middle
        else:
            start, end = middle+1, len(words)   # 찾으려는 단어가 위쪽 절반에 위치
            
        words =  words[start : end]
        
if __name__ == '__main__':
    f = open('Korean_lorem.txt', 'r', encoding='cp949')
    lorem = f.read()
    word_list = lorem.split()
    word_list.sort()
    print(findword('헌법재판소는', word_list))
    
    max_count = 0
    total_search_count = 0

    for word in word_list: 
        count = findword(word, word_list)
        if count > max_count:
            max_count = count
        total_search_count += count
    
    average_count = total_search_count / len(word_list)
    print("max_count =", max_count)
    print("average_count =", average_count)

        
        
    