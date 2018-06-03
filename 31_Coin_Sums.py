


# this is convoluted and took me forever to figure out
def ways_to_change_money_recursion(cents, coin_list, ways):
    for i, coin in enumerate(coin_list):

        num_coins = cents // coin
        remaining_cents = cents % coin

        if num_coins == 0:
            continue

        elif remaining_cents == 0:
            ways+=1

        elif remaining_cents >0:
            ways = ways_to_change_money_recursion(remaining_cents, coin_list[i + 1:], ways)

        if  num_coins > 0 and coin != 1:
            same_coint_count = num_coins -1
            while same_coint_count > 0:
                leftover =  cents - coin * (same_coint_count)
                ways = ways_to_change_money_recursion(leftover, coin_list[i + 1:], ways)
                same_coint_count -= 1

    return ways



# i looked up this solution after, and its so much easier
def ways_to_change_money_dynamic(cents, coin_list):

    ways = [0] * (cents + 1)
    ways[0] = 1
    for i in range(len(coin_list)):
        j = coin_list[i]
        while j <= cents:

            ways[j] += ways[j-coin_list[i]]
            j+=1

    return ways[-1]



cents = 100

coin_list_us_1 = [50,25, 10, 5, 1]
coin_list_uk_1 = [200, 100, 50, 20, 10, 5, 2, 1]

coin_list_us_2 = [1, 5, 10, 25, 50]
coin_list_uk_2 = [1, 2, 5, 10, 20, 50, 100, 200]


print(ways_to_change_money_recursion(cents, coin_list_us_1, 0))
print(ways_to_change_money_dynamic(cents, coin_list_us_2))