#Question 8: AlternatingPath
#Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.
import collections
def AlternatingPath(origin, destination, g):

    q = collections.deque()
    distance = 0
    q.append((origin, '', distance))
    visited = set()
    distance = 0
    while q:
        n, color = q.pop()

        if n == destination:
            return distance
        if (n,color)in visited:
            continue

        visited.add((n,color))

        for neighbor in g[n]:
            if color != neighbor[1]:
                q.append((neighbor[0], neighbor[1],distance + 1))
        
    return -1
    

   



    

        



