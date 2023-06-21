
def adjacencySet(edges):
    adjList = {}

    for edge in edges:

        source,destination = edge

        if source not in adjList:
            adjList[source] = []

        adjList[source].append(destination)

        if destination not in adjList:
            adjList[destination] = []

    for node in adjList:
        adjList[node] == sorted(adjList[node])
         

    return dict(sorted(adjList.items()))


# BFS 

def bfs(target, g):

    visited = []
    queue = []

    for node in g:
        if node not in visited:
            queue.append(node) 
           
        while queue:
            curr_node = queue.pop(0)

            if curr_node == target:
                return True
            visited.add(curr_node)

            neighbors = g[curr_node]
   
            if neighbors:
                for neighbor in neighbors :
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

    return False

#DFS

def dfs(target, g):
    visited = []

    stack = []

    for node in g:
        if node not in visited:
            stack.append(node)
    
        while stack:
            print(stack)
            curr_node = stack.pop()
      
            if curr_node == target:
                return True
        
            visited.append(curr_node)
            neighbors = g[curr_node]
          
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)

    return False


#Topological sorting

def recursiveTopological(g,curr_node, stack, visited):
    visited.append(curr_node)

    neighbors = g[curr_node]

    for neighbor in neighbors:
        if neighbor not in visited:
            recursiveTopological(g, neighbor, stack, visited)

    stack.append(curr_node)


def topologicalSort(g):
    stack = []
    visited = []

    for node in g:
        if node not in visited:
            recursiveTopological(g,node,stack,visited)

    return stack[::-1]
  

def main():
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    g = adjacencySet(edges)
    print(g)
  
    #print(bfs(3, g))
    #print(dfs(33,g))

    g1= {5: [2,0],
         2:[3],
         3:[1],
         4:[0,1],
         0:[],
         1:[]}
    
    print(topologicalSort(g1))
'''Output:
{
    0: []
    1: [2, 3]
    2: [0, 3]
    3: [2]
}'''



if __name__ == '__main__':
    main()







