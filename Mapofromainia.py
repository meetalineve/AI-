from queue import Queue

romaniaMap = {
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86}
}


def bfs(startingNode, destinationNode):
    visited = {}  # For keeping track of visited nodes
    distance = {}  # For keeping track of distance from startingNode
    parent = {}  # For keeping track of parent nodes in the traversal

    bfs_traversal_output = []
    queue = Queue()

    # Initialize visited, distance, and parent for each node
    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in romaniaMap[u].keys():
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + romaniaMap[u][v]
                queue.put(v)

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    total_distance = distance[destinationNode]
    print("Shortest path to reach the destination:")
    print(path)
    print("Total distance traveled:", total_distance)


# Take input from the user for starting and destination cities
startingCity = input("Enter the starting city: ")
destinationCity = input("Enter the destination city: ")

# Call the BFS function with user input
bfs(startingCity, destinationCity)
