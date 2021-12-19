## Problem
#REQ: Starting with a 1-indexed array of zeros
#REQ: Given a list of triples: start_idx, end_idx, value_to_add
#REQ: Indices are inclusive
#REQ: For every triple, add "value_to_add" to the starting array at corresponding indices
#REQ: Return the maximum value in the array 


def arrayManipulation(n, queries):
    new_array = [0] * (n + 2)
    for i in range(len(queries)):
        start_idx = queries[i][0]
        end_idx = queries[i][1]
        value = queries[i][2]

        new_array[start_idx] += value
        new_array[end_idx + 1] -= value
    
    max_value = float("-inf")
    sum_value = 0
    for value in new_array:
        sum_value += value
        max_value = max(max_value, sum_value)

    return max_value


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []
    
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)