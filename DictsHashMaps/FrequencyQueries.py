import argparse
from collections import defaultdict
from typing import List


def freqQuery(queries: List[List[int]]) -> List[int]:
    result = []
    counter = defaultdict(int)
    for query in queries:
        operation, value = query
        if operation == 1:
            counter[value] += 1
        if operation == 2:
            counter[value] -= 1
        if operation == 3:
            if value in counter.values():
                result.append(1)
            else:
                result.append(0)
    return result


if __name__ == "__main__":
    def queries(qs):
        try: 
            x, y = map(int, qs.split(","))
            return x, y
        except:
            raise argparse.ArgumentTypeError("Queries must be x,y")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=int) 
    parser.add_argument("-arr", dest="arr", type=queries, nargs="+")
    args = parser.parse_args()
    queries = []
    for t in args.arr:
        queries.append(list(t))
    results = freqQuery(queries)
    print(results)

    # Test Inputs:
    # python3 DictsHashMaps/FrequencyQueries.py -q 8 -arr 1,5 1,6 3,2 1,10 1,10 1,6 2,5 3,2
    # python3 DictsHashMaps/FrequencyQueries.py -q 10 -arr 1,3 2,3 3,2 1,4 1,5 1,5 1,4 3,2 2,4 3,2
