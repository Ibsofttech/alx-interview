#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given.
    """
    if total <= 0:
        return 0
    remain = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remain > 0:
        if coin_idx >= n:
            return -1
        if remain - sorted_coins[coin_idx] >= 0:
            remain -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
