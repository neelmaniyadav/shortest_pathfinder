import heapq

def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    pq = [(0, start)]
    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Dictionary to store the path
    previous_nodes = {}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current = end
    
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    
    if path:
        path.insert(0, start)
    
    return path, distances[end]

# Example graph as an adjacency list
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 4, 'C': 8, 'D': 5},
    'C': {'A': 4, 'B': 7, 'D': 6},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'C'
path, distance = shortest_path(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {path} with distance {distance}")




