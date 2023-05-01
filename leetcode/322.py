from collections import deque


def coinChange(coins, amount):
    def dfs(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        min_coin_change = float("inf")

        for coin in coins:
            ret = dfs(amount - coin)
            if ret == -1:
                continue

            min_coin_change = min(min_coin_change, ret)

        return min_coin_change + 1 if min_coin_change != float("inf") else -1

    return dfs(amount)


def coinChange(coins, amount):
    memo = {}

    def dp(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        min_coin_change = float("inf")

        for coin in coins:
            if amount - coin not in memo:
                memo[amount-coin] = dp(amount - coin)

            ret = memo[amount-coin]
            if ret == -1:
                continue

            min_coin_change = min(min_coin_change, ret)

        return min_coin_change + 1 if min_coin_change != float("inf") else -1

    return dp(amount)


print(coinChange(coins=[10, 8, 2], amount=16))


# tabulation
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
print(s.coinChange(coins=[1, 2, 5], amount=11))


def coinChange(coins, amount):
    q = deque([(amount, [])])
    visited = set()
    # visited = {}
    # visited = [False] * (amount + 1)
    while q:
        cur_amount, used_coins = q.popleft()
        if cur_amount == 0:
            return used_coins
        for c in coins:
            next_amount = cur_amount - c
            next_used_coins = used_coins[:]
            if next_amount < 0:
                continue
            # if next_amount in visited or next_amount < 0:
            #     continue
            next_used_coins = used_coins[:]
            next_used_coins.append(c)
            q.append((next_amount, next_used_coins))
            visited.add(next_amount)

    return -1


def coinChange(coins, amount):
    q = deque([(amount, 0)])
    visited = set()
    # visited = {}
    # visited = [False] * (amount + 1)
    while q:
        cur_amount, used_coins = q.popleft()
        if cur_amount == 0:
            return used_coins
        for c in coins:
            next_amount = cur_amount - c
            if next_amount < 0:
                continue
            # if next_amount in visited or next_amount < 0:
            #     continue

            q.append((next_amount, used_coins + 1))
            visited.add(next_amount)

    return -1


print(coinChange(coins=[5, 2, 1], amount=11))
