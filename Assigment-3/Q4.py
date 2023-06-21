#Question 4: NumberOfIslands
#Given a binary matrix in which 1s represent land and 0s represent water. Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
#Graph: Breadth-First Traversal
#Time-complexity: O(rows*columns),  Space-complexity: O(rows*columns)
import collections
def numberOfIslands(matrix):

    if not matrix:
        return 0
        
    rows, columns = len(matrix), len(matrix[0])
    visited = set()
    islands = 0

    def bfs(row,column):
        q = collections.deque()
        visited.add((row,column))
        q.append((row,column))

        while q:
            r,c = q.popleft()
            #for each value, we need to check left,right,top, and bottom
            directions = [[1,0],[0,1],[-1,0], [0,-1]]

            for dr,dc in directions:
                curr_row, curr_col = r + dr, c+ dc

                if (curr_row in range(rows) and
                    curr_col in range(columns) and  
                    matrix[curr_row][curr_col] == 1 and 
                    (curr_row, curr_col) not in visited):
                    
                    q.append((curr_row,curr_col))
                    visited.add((curr_row, curr_col))
                    
                    
    for row in range(rows):
        for column in range(columns):
            #if the value is island and has not yet been visited, we perform bfs
            if matrix[row][column] == 1 and (row, column) not in visited:
                bfs(row, column)
                islands += 1

    return islands

        
def main():
    g1= [[1,0,1,1,1],
        [1,1,0,1,1],
        [0,1,0,0,0],
        [0,0,0,1,0],
        [0,0,0,0,0]]
    g2 = [[1,0,0],
        [0,0,0]]
    

    g = [[1,1,1,1,0],
         [1,1,0,1,0],
         [1,1,0,0,0],
          [0,0,0,0,0]]
  
    g3= [[1,1,1,1,1],
         [0,0,0,0,0],
        [1,1,1,1,1]]
    
    g4 = [[1,0,1],
          [0,1,0],
          [1,0,1]]
    
    g5 = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]
    
    island = numberOfIslands(g5)
    print("Islands: ", island)
        

if __name__ == '__main__':
        main()

#Time-spent: 1 hour


  

