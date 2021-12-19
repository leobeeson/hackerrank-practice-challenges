

def countSwaps(a):    
    swaps_counter = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
               a[j], a[j + 1] = a[j + 1], a[j]
               swaps_counter += 1
    print(f"Array is sorted in {swaps_counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)