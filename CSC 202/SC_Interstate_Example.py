from pythonds3.graphs.adjacency_graph import Graph, Vertex

def add_2way_edge(g: Graph, v1: Vertex, v2: Vertex, w: int) -> None:
    """In the graph G, add an edge from V1 to V2 with weight W,
       and another edge from V2 to V1 witht the same weight."""
    g.add_edge(v1, v2, w)
    g.add_edge(v2, v1, w)

def build_SC_interstates() -> Graph:
    edges = [('ATL', 'GVL', 145), ('AUG', 'CLB', 76), ('SAV', 'WTL', 100),
             ('GVL', 'CNN', 44), ('GVL', 'SPB', 33), ('CNN', 'CLB', 62),
             ('CNN', 'SPB', 36), ('CLB', 'WTL', 61), ('CLB', 'CLT', 93),
             ('CLB', 'FLO', 83), ('WTL', 'CHS', 57), ('WTL', 'FLO', 86),
             ('SPB', 'CLT', 74), ('FLO', 'MYR', 68), ('FLO', 'FVL', 88)]
    result = Graph()

    for edge in edges:
        add_2way_edge(result, edge[0], edge[1], edge[2])
    return result

def print_graph(g: Graph) -> None:
    for key in g.get_vertices():
        vertex = g.get_vertex(key)
        print(vertex, end='| ')
        for neighbor in vertex.get_neighbors():
            print(neighbor.get_key(), vertex.get_neighbor(neighbor), end='; ')
        print()

def main(args: list[str]) -> int:
    g = build_SC_interstates()
    assert len(g.get_vertices()) == 13
    assert len(g.get_edges()) == 30
    print_graph(g)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# This code is made by Dr. Peter Brown. This code is NOT mine.