import sys


def solve(c, n, weights, values, limits):
    status = [0] * (c + 1)
    limits_check = []
    for _ in range(c + 1):
        limits_check.append([0] * n)

    for j in range(1, c + 1):
        for i in range(n):
            j_minus = j - weights[i]
            if j_minus >= 0:
                if limits_check[j_minus][i] < limits[i]:
                    if status[j_minus] + values[i] > status[j]:
                        status[j] = status[j_minus] + values[i]
                        limits_check[j] = limits_check[j_minus].copy()
                        limits_check[j][i] += 1
                # else:
                #     if status[j_minus] > status[j]:
                #         status[j] = status[j_minus]
                #         limits_check[j] = limits_check[j_minus].copy()

    return status[-1]


if __name__ == '__main__':
    c= 10
    n = 3
    weights =[ 1, 3, 4]
    values = [15,20,30]
    limits = [ 2, 3, 2]
    # weights =[ 4, 3, 1]
    # values = [30,20,15]
    # limits = [ 2, 3, 2]

    print(solve(c, n, weights, values, limits))
    while True:
        try:
            raw_data = [input().strip().split(" ") for _ in range(4)]
            data = [[int(x) for x in r] for r in raw_data]
            c = data[0][0]
            n = data[0][1]
            weights = data[1]
            values = data[2]
            limits = data[3]
            print(solve(c, n, weights, values, limits))
        except EOFError:
            break
