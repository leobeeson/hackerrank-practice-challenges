from typing import List


def roadsAndLibraries(n: int, c_lib: int, c_road: int, city_edges: List[List[int]]) -> int:
    
    total_cost = 0
    
    if n == 0:
        return total_cost
    if n == 1:
        return c_lib
    if c_road >= c_lib:
        return c_lib * n
    
    city_ids = range(1, n + 1)

    city_adjacency_list = {city_id: {city_id} for city_id in city_ids}
    
    for city_edge in city_edges:
        city_a = city_edge[0]
        city_b = city_edge[1]
        city_adjacency_list[city_a].add(city_b)
        city_adjacency_list[city_b].add(city_a)
    
    city_components = []
    visited_cities = set()

    for city_id in city_ids:
        if city_id in visited_cities:
            continue
        visited_cities.add(city_id)

        current_city_component = set()
        current_city_neighbours = city_adjacency_list[city_id]

        queue = [current_city_neighbours]
        while queue:
            city_neighbours = queue.pop()
            current_city_component.update(city_neighbours)

            for city_neighbour in city_neighbours:
                if city_neighbour in visited_cities:
                    continue
                visited_cities.add(city_neighbour)
                next_city_neighbours = city_adjacency_list[city_neighbour]
                queue.append(next_city_neighbours)

        city_components.append(current_city_component)

    for component in city_components:
        total_cost += c_lib
        total_cost_of_roads = (len(component) - 1) * c_road
        total_cost += total_cost_of_roads

    return total_cost
  
         
# [[1,7],[1,3],[1,2],[2,3],[5,6]]
if __name__ == "__main__":
    q = int(input().strip())
    
    for q_itr in range(q):

        multiple_input = input().rstrip().split()

        n = int(multiple_input[0])
        m = int(multiple_input[1])
        c_lib = int(multiple_input[2])
        c_road = int(multiple_input[3])

        city_edges = []

        for  _ in range(m):
            edges = list(map(int, input().rstrip().split()))
            city_edges.append(edges)

        result = roadsAndLibraries(n, c_lib, c_road, city_edges)

        print(result)
