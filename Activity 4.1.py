def integer(x):
    for i in range(x):
        print(i)


integer(21)

print("\n")


def sum(y):
    for i in range(y):
        y = y + i
    print(y)


sum(100)


print("\n")


def fact(m):
    t = 1
    for i in range(m-1):
        m = m * t
        t = t + 1
    print(m)

fact(0)
fact(1)
fact(2)
fact(3)
fact(4)
fact(5)


