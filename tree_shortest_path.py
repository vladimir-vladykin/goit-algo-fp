import networkx as nx
import heapq

# Kharkiv subway stations
# green line
peremoga = "Перемога"
naukova = "Наукова"
derzhprom = "Держпром"
architect = "Архітектора\nБекетова"
metro_bud = "Метробу-\nдівників"
green_line = [peremoga, naukova, derzhprom, architect, metro_bud]
green_travel_time_min = [10, 3, 5, 7]

# blue line
history_museum = "Історичний\nмузей"
university = "Університет"
yaroslav = "Ярослава\nМудрого"
kyiv = "Київська"
akademic = "Академіка\nБалашова"
student = "Студентська"
blue_line = [history_museum, university, yaroslav, kyiv, student]
blue_travel_time_min = [4, 2, 4, 9]

# red line
vokzal = "Вокзальна"
konst_maidan = "Майдан\nКонституції"
levada = "Левада"
sport = "Спортивна"
turbo_atom = "Турбоатом"
palaz_sport = "Палац\nспорту"
army = "Армійська"
red_line = [vokzal, konst_maidan, levada, sport, palaz_sport]
red_travel_time_min = [6, 3, 4, 6]

# intersections of lines
green_blue_intersection = [derzhprom, university]
green_red_intersection = [metro_bud, sport]
blue_red_intersection = [history_museum, konst_maidan]

def main():
    # setup graph of Kharkiv subway stations
    kharkiv_subway_stations_graph = create_subway_graph()

    # calculate path
    shortest_path = dijkstra_shortest_path(kharkiv_subway_stations_graph, peremoga)

    # display path
    print(f"Shortest path for subway graph:\n{shortest_path}")


# find shortest path to visit every node
def dijkstra_shortest_path(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


def create_subway_graph():
    # setup graph
    kharkiv_subway_stations_graph = nx.Graph()

    # add nodes
    kharkiv_subway_stations_graph.add_nodes_from(green_line)
    kharkiv_subway_stations_graph.add_nodes_from(blue_line)
    kharkiv_subway_stations_graph.add_nodes_from(red_line)

    # add edges for each line, with travel time as weight
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_line, weights = green_travel_time_min))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(blue_line, weights=blue_travel_time_min))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(red_line, weights=red_travel_time_min))

    # add edges for line intersections
    # intersections always have travel_time = 1 minute
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_blue_intersection, weights = [1]))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(green_red_intersection, weights = [1]))
    kharkiv_subway_stations_graph.add_weighted_edges_from(array_to_pairs(blue_red_intersection, weights = [1]))

    return kharkiv_subway_stations_graph

# turn arrays like '[1, 2, 3, 4]' into array of pair tuples,
# like [(1, 2), (2, 3), (3, 4)].
# in case when weights presented, adds it as third element of each tuple
def array_to_pairs(array: list, weights: list = None) -> list:
    if len(array) <= 1:
        # impossible to build arrays of pairs
        return []
    
    result = []
    for i in range(1, len(array)):
        first = array[i - 1]
        second = array[i]

        if weights is not None:
            result.append((first, second, weights[i - 1]))
        else:
            result.append((first, second))

    return result

if __name__ == "__main__":
    main()