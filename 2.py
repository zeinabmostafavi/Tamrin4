x = int(input('rows: '))
y = int(input(' columns: '))


def chess():
    for m in range(x):
        temp = []
        for n in range(y):
            if (m + n) % 2 == 0:
                temp.append('*')
                print('*', end=' ')
            else:
                print('#', end=' ')
                temp.append('#')
        print()


chess()
