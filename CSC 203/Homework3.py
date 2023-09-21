from pythonds3.graphs.adjacency_graph import Graph, Vertex
from pythonds3.basic import Queue

# This graph is directed and asymmetric.
def add_1way_edge(g: Graph, v1: Vertex, v2: Vertex) -> None:
    g.add_edge(v1, v2)

# This builds the requirements for each course.
# Please note that I've put v1 as the course in question, and v2 as the requirement.
def build_CS_Requirements() -> Graph:
    edges = [('MTH 108', 'MTH 117'),
             ('MTH 110', 'MTH 120'),('MTH 110', 'CSC 201'),
             ('CSC 201', 'CSC 202'),('CSC 201', 'CSC 235'),('CSC 201', 'MTH 205'),
             ('CSC 235', 'CSC 335'),
             ('CSC 202', 'CSC 321'),('CSC 202', 'CSC 203'),('CSC 202', 'CSC 392'),('CSC 202', 'CSC 350'),('CSC 202', 'CSC 355'),
             ('CSC 321', 'CSC 322'),
             ('CSC 392', 'CSC 492')]
    result = Graph()

# This forms the resulting edges.
    for edge in edges:
        add_1way_edge(result, edge[0], edge[1])
    return result

# This prints the graph.
def print_graph(g: Graph) -> None:
    for key in g.get_vertices():
        vertex = g.get_vertex(key)
        print(vertex, end='| ')
        for neighbor in vertex.get_neighbors():
            print(neighbor.get_key(), vertex.get_neighbor(neighbor), end='; ')
        print()

def reset_graph(g: Graph) -> None:
    for key in g.get_vertices():
        v = g.get_vertex(key)
        v.set_color('white')
        v.set_distance = sys.maxsize
        v.set_previous(None)

# This is the main function.
def main(args: list[str]) -> int:
    g = build_CS_Requirements()
    assert len(g.get_vertices()) == 16
    assert len(g.get_edges()) == 14
    print_graph(g)

    for start_key in g.get_vertices():
        v_start = g.get_vertex(start_key)
        g.dfs()
        for end_key in g.get_vertices():
            if end_key != start_key:
                v_end = g.get_vertex(end_key)
                if v_end.get_previous() != None:
                    g.traverse(start_key, end_key)
                else:
                    print("No path from", start_key, "to",  end_key, ".")
        reset_graph(g)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# My work is based on the explanation from class by Dr. Peter Brown.