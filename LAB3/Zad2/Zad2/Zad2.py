import heapq

def dijkstra(graph, start):
    distance = {top: float('inf') for top in graph}
    distance[start] = 0

    queue = [(0,start)]

    while queue:
        curr_dist, curr_top = heapq.heappop(queue)

        if curr_dist>distance[curr_top]:
            continue
        for neighbour, cost in graph[curr_top].items():
            new_dist = curr_dist + cost
            if new_dist < distance[neighbour]:
                distance[neighbour] = new_dist
                heapq.heappush(queue, (new_dist, neighbour))
    return distance

graph={
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
    }

result = dijkstra(graph,'A')
print(result)
