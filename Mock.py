'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.'''

from collections import deque

def numberOfIslands(grid):


    q = deque()
    visited = set()
    directions = [(1,0),(0,1), (-1,0),(0,-1)]

    def bfs(r,c):
        q.append(r,c)

        while q:
            r1, c1 = q.pop()
            #visited.add((r1,c1))

            for dr,dc in directions:
                row, col = r1+dr, c1 + dc

                if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == "1" and (row, col) not in visited:
                    q.append((row,col))
                    visited.add((r1,c1))



    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    #directions = [(1,0),(0,1), (-1,0),(0,-1)]

    for r in rows:
        for c in cols:

            if grid[r][c] == "1" and grid[r][c] not in visited:

                bfs(r,c)
                islands +=1

    return islands







    

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3