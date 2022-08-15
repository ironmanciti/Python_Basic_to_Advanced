# HTML 에서 BABY 이름 찾기
"""
step 1 - https://developers.google.com/edu/python/exercises/baby-names 에서
file download 하여 babynames directory 로 save

step 2 - <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td> 에
match 되는 정규표현식을 이용하여 (rank, boy-name, girl-name) tuples 추출하여
print

"""
import sys
import re

def extract_name(filename):
    names = []
    f = open(filename, 'r')
    text = f.read()
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for tup in tuples:
        print(tup[0], tup[1], tup[2])

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("file 명을 parameter 로 입력 바랍니다.")
        sys.exit(1)

    filename = './babynames/' + args[0]
    extract_name(filename)
