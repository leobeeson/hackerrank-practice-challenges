import argparse

def jumping_on_clouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i+2 < len(c) and c[i+2] == 0:
            jumps += 1
            i += 2
            continue
        jumps += 1
        i += 1
    return jumps






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", metavar="s", type=int, nargs="+")
    args = parser.parse_args()
    answer = jumping_on_clouds(args.c)
    print(answer)