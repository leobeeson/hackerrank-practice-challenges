# arr = [3, 7, 4, 6, 5]

def maxSubsetSum(arr):
    if len(arr) == 0:
        return 0
    
    if sum(arr) < 0:
        return 0

    if all(i < 0 for i in arr):
        return arr[0]
    
    maximums = [0]*len(arr)
    
    maximums[0] = max(0, arr[0])
    maximums[1] = max(maximums[0], arr[1])

    for i in range(2, len(arr)):
        maximums[i] = max(maximums[i-1], arr[i] + maximums[i-2])

    return maximums[-1]   


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = maxSubsetSum(arr)
    print(result)