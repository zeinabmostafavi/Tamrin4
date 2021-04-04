def table(a, b):
    for i in range(1, a + 1):
        for j in range(1, b+1):
            print(i * j, end=' ')
        print()

        a = int(input("number col : "))
        b = int(input("number row : "))
        table(a, b)
