
def minimum_bribes(q):
    num_bribes = 0
    for i in range(len(q) - 1, 0, -1):
        if q[i] != (i + 1):    
            if q[i-1] == (i + 1):
                num_bribes += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == (i + 1):
                num_bribes += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]
            else:
                print("Too chaotic")
                return
    print(num_bribes)


if __name__ == "__main__":    
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
