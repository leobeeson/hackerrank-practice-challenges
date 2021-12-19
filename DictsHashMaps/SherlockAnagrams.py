

def sherlockAndAnagrams(s):
    substrings_dict = {}
    num_letters = len(s)
    for left_pointer in range(num_letters):
        for right_pointer in range(left_pointer + 1, num_letters + 1):
            substring = s[left_pointer:right_pointer]
            if substring in substrings_dict:
                substrings_dict[substring] += 1
            else:
                substrings_dict[substring] = 1

    sorted_substrings_dict = {}
    for k, v in substrings_dict.items():
        k_sorted = "".join(sorted(k))
        if k_sorted in sorted_substrings_dict:
            sorted_substrings_dict[k_sorted] += v
        else:
            sorted_substrings_dict[k_sorted] = v

    counter = 0
    for k, v in sorted_substrings_dict.items():
        if v > 1:
            counter += (v*(v - 1))/2
        
    return(int(counter))




if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)