#Question 11: VacationDestinations
#Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other 
#with corresponding travel times in hours, return the number of destinations within k hours of the origin. 
#Assume that having a stopover in a city adds an hour of travel time.
#Time- complexity: 0(V + E), Space-complexity: 0(N)

def adjList(arr):

    map_cities = {}

    for city1, city2, dist in arr:

        if city1 not in map_cities:
            map_cities[city1] = []

        map_cities[city1].append((city2,dist))

        if city2 not in map_cities:
            map_cities[city2] = []

        map_cities[city2].append((city1,dist))

    return map_cities


def vacationDestinations(origin,k, arr):

    mapped_cities = adjList(arr)
    visited = set()
    possible_destinations = []

    def dfs(city,d, k):

        visited.add(city)
        neighbors = mapped_cities[city]
      
        for neighbor, distance in neighbors:
            if neighbor not in visited and d + distance <= k:
                possible_destinations.append(neighbor)
                dfs(neighbor, d+ distance + 1, k)


    dfs(origin, 0, k)
    return possible_destinations
    

def main():
    arr_cities = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), 
("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    
    print(vacationDestinations('New York', 8, arr_cities))
    print(vacationDestinations('New York', 5, arr_cities))
    print(vacationDestinations('New York', 7, arr_cities))
    #print(adjList(arr_cities))


if __name__ == "__main__":
    main()
'''Input: [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), 
("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

Origin = "New York", k=5
Output: 2 (["Boston", "Philadelphia"])

Origin = "New York", k=7
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

Origin = "New York", k=8
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])'''