import heapq

# Define weighted undirected graph
graph = {
    'a': [('b', 4), ('h', 8)],
    'b': [('a', 4), ('c', 8), ('h', 11)],
    'c': [('b', 8), ('d', 7), ('f', 4), ('i', 2)],
    'd': [('c', 7), ('e', 9), ('f', 14)],
    'e': [('d', 9), ('f', 10)],
    'f': [('c', 4), ('d', 14), ('e', 10), ('g', 2)],
    'g': [('f', 2), ('h', 1), ('i', 6)],
    'h': [('a', 8), ('b', 11), ('g', 1), ('i', 7)],
    'i': [('c', 2), ('g',6),('h',7)]
}

def prim_mst(start):
    visited = set()
    min_heap = []
    mst = []
    total_cost = 0

    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap:
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            total_cost += weight
            for next_neighbor, next_weight in graph[to]:
                if next_neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, to, next_neighbor))

    print("Prim's MST Edges:")
    for edge in mst:
        print(edge)
    print(f"Total MST Cost: {total_cost}")

# Run Prim's algorithm starting from node 'A'
prim_mst('i')
