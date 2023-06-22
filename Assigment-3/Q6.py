'''Question 6: RoadNetworks
In some states, it is not possible to drive between any two towns because they are not connected to the same road network.
 Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. 
 (For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the towns 
 are connected by roads has 0 road networks.)'''

#Graph: DFS
#Time-complexity: O(V+E), Space-complexity: 0(V) where V is vertices and E is edges
import collections

def adjacencySet(cities, edges):
    adjList = {}
    for city in cities:
        adjList[city] = []

    for edge in edges:
        city1, city2 = edge
        if city1 not in adjList:
            adjList[city1] = []
            adjList[city1].append(city2)
        if city2 not in adjList:
            adjList[city2] = []
            adjList[city2].append(city1)
        adjList[city1].append(city2)
        adjList[city2].append(city1)

    for node in adjList:
        adjList[node] = sorted(adjList[node])

    return adjList


def RoadNetworks(cities, edges):
    paths = adjacencySet(cities,edges)
    road_networks = 0
    visited = set()

    def dfs(city):
        visited.add(city)

        if city in paths:
            for neighbor in paths.get(city,[]):
                if neighbor not in visited:
                    dfs(neighbor)

    for city in cities:
        if city not in visited:
            dfs(city)
            
            if city in paths and len(paths[city]) > 0:
                road_networks += 1

    return road_networks



def main():
   c = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"]
   p = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
   print(adjacencySet(c,p))
   print(RoadNetworks(c,p))

   t=["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
   e= [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
   print(RoadNetworks(t,e))

   c = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"]
   d = []
   print(RoadNetworks(c,d))


   

if __name__ == "__main__":
    main()