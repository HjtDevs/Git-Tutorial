from module import *

def main():
    print('Hello, World!')
    counter = Counter(1, 1, -1)
    counter()
    counter()
    counter()
    counter(False)
    print(counter.count)

if __name__ == '__main__':
    main()