import sys
import re

def extract_name(filename):
    names = []
    f = open(filename, 'r')
    text = f.read()
    tuples = re.findall(r'<td>(\d)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for tup in tuples:
        print(tup[0], tup[1], tup[2])

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("file 명 미입력")
        sys.exit(1)
    filename = './babynames/' + args[0]
    extract_name(filename)
