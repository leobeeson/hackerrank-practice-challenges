


def whatFlavors(cost, money):
    # There's always a unique answer, but initiate just in case all trys fail:
    ice_cream_a = 0
    ice_cream_b = 0

    ice_cream_menu = {}

    for ice_cream_a_index in range(len(cost)):
        ice_cream_a_price = cost[ice_cream_a_index]
        ice_cream_b_budget = money - ice_cream_a_price

        try:
            ice_cream_b_index = ice_cream_menu[ice_cream_b_budget]
            ice_cream_a = ice_cream_a_index + 1
            ice_cream_b = ice_cream_b_index + 1
            break
        except KeyError:
            pass

        ice_cream_menu[ice_cream_a_price] = ice_cream_a_index
    
    if ice_cream_a < ice_cream_b:
        print(f"{ice_cream_a} {ice_cream_b}")
    else:
        print(f"{ice_cream_b} {ice_cream_a}")


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
