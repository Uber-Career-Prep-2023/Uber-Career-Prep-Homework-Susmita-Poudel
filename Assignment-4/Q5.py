#Question 5: MinCostStairClimbing
'''A staircase on a hiking trail implements a rather unusual toll system to cover trail maintenance costs. 
Each stair in the staircase has a different toll which you only have to pay if you step on that stair. 
Due to the height of the stairs, you can only climb one or two stairs at once. This means that from the ground 
you must initially step on either stair 0 or stair 1 and that, if there are n stairs, the last stair you step on 
can be either stair n-1 or n-2. Given an array representing the costs per stair, what is the minimum possible toll you 
can pay to climb the staircase?'''

#Time-complexity: 0(n)     Space-complexity: 0(n), where n is len of the cost array
def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)  # Initialize an array to store the minimum cost to reach each stair
    
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    
    return dp[n]

def main():
    cost1 = [4, 1, 6, 3, 5, 8]
    print(minCostClimbingStairs(cost1))  # Output: 9

    cost2 = [11, 8, 3, 4, 9, 13, 10]
    print(minCostClimbingStairs(cost2))  # Output: 25


if __name__ == '__main__':
        main()
