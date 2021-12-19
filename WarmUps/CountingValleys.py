import argparse


def counting_valleys(steps, path):
    valleys = 0
    depth = 0
    for step in path:
        if step == "D":
            depth -= 1
        elif step == "U" and depth == -1:
            valleys += 1
            depth += 1
        else:
            depth += 1

    return valleys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", metavar="s", type=int)
    parser.add_argument("--path", metavar="p", type=str)
    args = parser.parse_args()
    answer = counting_valleys(args.steps, args.path)
    print(answer)
