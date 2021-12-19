
# arr = [1, 3, 9, 9, 27]
# r = 3

def countTriplets(arr, r):
    rights_dict = {}
    lefts_dict = {}
    triples_counter = 0
    
    for item in arr:
        try:
            rights_dict[item] += 1
        except KeyError:
            rights_dict[item] = 1    

    for item in arr:
        geom_to_left = item // r
        geom_to_right = item * r

        rights_dict[item] -= 1
        
        try:
            occurrences_left_side = lefts_dict[geom_to_left]
        except KeyError:
            occurrences_left_side = 0
        
        try:
            occurrences_right_side = rights_dict[geom_to_right]
        except KeyError:
            occurrences_right_side = 0

        if occurrences_left_side > 0 and occurrences_right_side > 0 and item % r == 0:
            triples_counter += occurrences_left_side * occurrences_right_side

        try:
            lefts_dict[item] += 1
        except KeyError:
            lefts_dict[item] = 1

    return triples_counter
    

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    result = countTriplets(arr, r)

    print(result)    