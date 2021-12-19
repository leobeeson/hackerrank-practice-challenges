import argparse



def sock_merchant(n, ar):
    num_pairs = 0
    socks_map = {}

    for sock in ar:
        try:
            _ = socks_map[sock]
            num_pairs += 1
            socks_map.pop(sock)
        except KeyError:
            socks_map[sock] = 1

    return num_pairs

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--array_size", metavar="n", type=int)
    parser.add_argument("--array", metavar="ar", type=int, nargs="+")
    args = parser.parse_args()
    answer = sock_merchant(args.array_size, args.array)
    print(answer)



