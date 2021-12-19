

def rotate_left(a, d):
    rot_a = a[d: ] + a[:d]
    return rot_a



if __name__ == "__main__":

    first_input = input().rstrip().split()
    n = int(first_input[0])
    d = int(first_input[1])
    a = list(map(int, input().rstrip().split()))

    result = rotate_left(a, d)
    print(result)