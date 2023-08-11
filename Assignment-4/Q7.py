#Question 7: LargestSquareOf1s
#Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

#Time-complexity: 0(rows* columns)  Space- complexity: 0(rows*columns)
def largestSquareOf1s(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[1] * cols for _ in range(rows)]
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                max_side = max(max_side, dp[i][j])
    
    return max_side

# Testcases
matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
print(largestSquareOf1s(matrix1))  # Output: 2

matrix2 = [
    [0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0]
]
print(largestSquareOf1s(matrix2))  # Output: 3



