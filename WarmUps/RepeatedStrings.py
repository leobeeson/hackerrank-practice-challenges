import argparse

def repeated_strings(s, n):
    a_in_pattern = s.count("a")
    pattern_length = len(s)
    
    full_pattern_count = n // pattern_length
    partial_pattern_length = n % pattern_length

    partial_pattern_string = s[:partial_pattern_length]
    a_in_partial_pattern = partial_pattern_string.count("a")

    a_in_string = a_in_pattern * full_pattern_count
    a_in_string += a_in_partial_pattern

    return a_in_string



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", metavar="s", type=str)
    parser.add_argument("--n", metavar="s", type=int)
    args = parser.parse_args()
    answer = repeated_strings(args.s, args.n)
    print(answer)