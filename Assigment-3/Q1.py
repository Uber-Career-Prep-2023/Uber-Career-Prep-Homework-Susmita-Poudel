
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
         

    return adjList


# BFS 

def bfs(target, g):
    

def main():
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    print(adjacencySet(edges))
'''Output:
{
    0: []
    1: [2, 3]
    2: [0, 3]
    3: [2]
}'''



if __name__ == '__main__':
    main()







