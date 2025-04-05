import sys


def climb(n, m):
    ms = [0] * m
    ms[0] = 1
    for i in range(1, m):
        ms[i] = sum(ms[:i]) + 1

    for i in range(m, n):
        new_count = sum(ms)
        ms[(i - m) % m] = new_count

    return ms[(n - 1 - m) % m]


if __name__ == '__main__':
    for line in sys.stdin:
        a, b = line.split(' ')

        print(climb(int(a), int(b)))
