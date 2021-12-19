

def minimumAbsoluteDifference(arr):
    min_abs_delta = float("inf")
    arr.sort()
    for i in range(len(arr) - 1):
        candidate_min = abs(arr[i] - arr[i + 1])
        min_abs_delta = min(min_abs_delta, candidate_min)
    return min_abs_delta
        

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)