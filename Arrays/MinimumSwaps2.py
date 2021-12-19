## Problem
#REQ: Unordered 1-d array
#REQ: Consecutive integers E[1,2,3,...,n]
#REQ: Without duplicates
#REQ: Swap any two elements
#TODO: Find the minimum number of swaps required to sort the array in ascending order.


def minimum_swaps(arr):
    swaps = 0
    n = len(arr)
    i = 0
    while i < n:
        num = arr[i]
        index = num - 1 
        if index != i:
           arr[i], arr[index] = arr[index], arr[i]
           swaps += 1
        else:
            i += 1
    return swaps


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(f"Initial Array: {arr}")
    result = minimum_swaps(arr)
    print(result)
