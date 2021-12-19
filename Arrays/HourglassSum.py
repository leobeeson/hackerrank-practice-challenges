

def hourglass_sum(arr):
    max_hourglass = float("-inf")
    for r in range(len(arr) - 2):
        for c in range(len(arr[r]) - 2):
            hourglass_sum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2]
            print(hourglass_sum)
            max_hourglass = max(max_hourglass, hourglass_sum)
    return max_hourglass


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglass_sum(arr)
    print(result)


# # Failed test case:
# Input
# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5

# Output
# -6

# # Initial function:
# def hourglass_sum(arr):
#     one_d_list = []
#     for l in arr:
#         one_d_list.extend(l)

#     hourglass_indices = [0, 1, 2, 7, 12, 13, 14]
#     max_hourglass = float("-inf")
#     for i in range(len(one_d_list) - hourglass_indices[-1]):
#         temp_hourglass = sum([one_d_list[i + j] for j in hourglass_indices])
#         max_hourglass = max(max_hourglass, temp_hourglass)
        
#     return max_hourglass