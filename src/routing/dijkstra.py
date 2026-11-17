def dijkstra(adjacency, start, destination, speed):

    distances = {}
    previous = {}
    visited = []

    # Initial distances
    for node_id in adjacency.keys():
        distances[node_id] = float("inf")
    distances[start.id] = 0

    if destination.id not in distances:
        distances[destination.id] = float("inf")

    # Processing the distances
    current_node = start

    while current_node != destination:

        visited.append(current_node)
        adjacent = adjacency.get(current_node.id, [])
        for edge in adjacent:
            neighbour = edge.end
            if neighbour in visited:
                continue
            edge_time = edge.distance / speed
            new_distance = distances[current_node.id] + edge_time
            if new_distance < distances.get(neighbour.id, float("inf")):

                distances[neighbour.id] = new_distance
                previous[neighbour.id] = current_node.id
        minimum_distance = float("inf")
        minimum_distance_node = None

        for node_id in distances:
            node = None

            for edge_list in adjacency.values():
                for edge in edge_list:
                    if edge.start.id == node_id:
                        node = edge.start
                        break
                    if edge.end.id == node_id:
                        node = edge.end
                        break
                if node is not None:
                    break

            # Skip already visited nodes
            if node in visited:
                continue

            # Find the node with the smallest distance
            if distances[node_id] < minimum_distance:
                minimum_distance = distances[node_id]
                minimum_distance_node = node

        # No reachable unvisited node remains
        if minimum_distance_node is None:
            break

        current_node = minimum_distance_node

    # Final Process
    if destination.id not in previous and start.id != destination.id:
        print("The destination is unreachable.")
        return None, float("inf")

    # Reconstruct the path
    final_path = []

    current = destination.id

    final_path.append(current)

    while current != start.id:
        current = previous[current]
        final_path.append(current)

    final_path.reverse()

    total_time = distances[destination.id]

    print(f"The path would be {final_path}")
    print(f"Total time taken {total_time}s")

    return final_path, total_time