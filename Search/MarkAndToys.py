k = 7
prices = [1, 2, 3, 4]

def maximumToys(prices, k):
    prices_sorted = sorted(prices)
    budget = k
    toys = 0
    for price in prices_sorted:
        if budget - price <= 0:
            break
        budget -= price
        toys += 1
    return toys


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)