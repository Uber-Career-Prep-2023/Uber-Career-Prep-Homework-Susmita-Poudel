#Question 8: AlternatingPath
#Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.
#Graph - BFS Traversal
#Time-complexity: O(V + E). Space-complexity: 0(V)

import collections
def AlternatingPath(origin, destination, g):

    q = collections.deque()
    distance = 0
    q.append((origin, '', distance))
    visited = set()
    distance = 0
    while q:
        n, color,dist = q.popleft()

        if n == destination:
            return dist
        if (n,color)in visited:
            continue

        visited.add((n,color, dist))

        for neighbor, neighbor_color in g[n]:
            if color != neighbor_color:
                q.append((neighbor, neighbor_color,dist + 1))
        
    return -1
def adjacencyList(l):
    d = {}
    for i in range(len(l)):
        curr_val = l[i]

        if curr_val[0] not in d:
            d[curr_val[0]] = []
        d[curr_val[0]].append((curr_val[1], curr_val[2]))

    return d

def main():


    a= [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
       ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
       ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]
    g1= adjacencyList(a)
    print(AlternatingPath( 'A',"E",g1))
    print(AlternatingPath( "E", "D",g1))



if __name__ == "__main__":
    main()
   



    

        



