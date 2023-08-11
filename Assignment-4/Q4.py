#The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!. 
#Given a non-negative integer n, return the Catalan numbers 0-n.

#Time-complexity: 0(n^2)      Space-Complexity: 0(n)
def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan = [0]*(n+1)
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
 
    # Return last entry
    return catalan[n]
 
 

n = 5
for i in range(n+1):
    print(catalan(i), end=" ")

n = 1
for i in range(n+1):
    print(catalan(i), end=" ")