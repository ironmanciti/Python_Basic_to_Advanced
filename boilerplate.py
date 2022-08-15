import sys

def hello():
    print("Hello Python")
    
if __name__ == '__main__':
    hello()
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])