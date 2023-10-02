from pythonds3 import Graph, Vertex
from typing import cast

# Weighted, two-way
edges_SC_interstates: list[tuple] = \
    [('SPB', 'CLT', 74), ('CNN', 'SPB', 36), ('GVL', 'SPB', 33), 
     ('ATL', 'GVL', 145), ('GVL', 'CNN', 44), ('CNN', 'CLB', 62),
     ('AUG', 'CLB', 76), ('CLB', 'CLT', 93), ('CLB', 'WTL', 61), 
     ('CLB', 'FLO', 83), ('WTL', 'CHS', 57), ('SAV', 'WTL', 100),
     ('WTL', 'FLO', 86), ('FLO', 'MYR', 68), ('FLO', 'FVL', 88)]

def build_graph(edges: list[tuple], two_way: bool = False) -> Graph:
    g = Graph()
    for edge in edges:
        weight = 0
        if len(edge) > 2:
            weight = edge[2]
        g.add_edge(edge[0], edge[1], weight)
        if two_way:
            g.add_edge(edge[1], edge[0], weight)
    return g

def print_graph(g: Graph) -> None:
    for key in sorted(g.get_vertices()):
        vertex: Vertex = cast(Vertex, g.get_vertex(key))
        print(vertex, end='| ')
        for neighbor in vertex.get_neighbors():
            print(neighbor.get_key(), vertex.get_neighbor(neighbor), end='; ')
        print()

def find_cycles(g: Graph, start: Vertex) -> int:
    """Use breadth-first search to find cycles in an undirected graph."""
    cycles_found = 0
    
    # Breadth-first search
    start.distance = 0
    start.previous = None
    vert_queue = [start]
    while vert_queue:
        current_vert = vert_queue.pop(0)
        for neigh in current_vert.get_neighbors():
            if neigh.color == "white":
                neigh.color = "gray"
                neigh.distance = current_vert.distance + current_vert.get_neighbor(neigh)
                neigh.previous = current_vert
                vert_queue.append(neigh)
            elif neigh.color == 'gray':
                cycles_found += 1
                print("Cycle found.")
                if neigh.distance > current_vert.distance + current_vert.get_neighbor(neigh):
                    neigh.distance = current_vert.distance + current_vert.get_neighbor(neigh)
                    neigh.previous = current_vert
        current_vert.color = "black"

    return cycles_found

def main():
    g: Graph = build_graph(edges_SC_interstates, True)
    cycles: int = find_cycles(g, g.get_vertex('SPB'))
    print_graph(g)
    print(cycles, 'cycles found')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
