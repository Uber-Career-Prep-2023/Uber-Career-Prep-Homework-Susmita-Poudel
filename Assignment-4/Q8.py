
#Question 8: CoinChange
#Given a list of coin denominations and a target sum, return the number of possible ways to make change for that sum.
#time-complexity: O(amount*coins) space-complexity:(amount)
def coinChange(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # There's one way to make change for amount 0 (using no coins)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

def main():
    coins1 = [2, 5, 10]
    sum1 = 20
    print(coinChange(coins1, sum1))  # Output: 6

    sum2 = 15
    print(coinChange(coins1, sum2))  # Output: 3

if __name__ == "__main__":
    main()
