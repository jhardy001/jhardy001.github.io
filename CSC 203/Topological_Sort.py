from pythonds3.graphs.adjacency_graph import Graph, Vertex
from typing import cast

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

def topologicalsort(g: Graph) -> None:
    topolist = []
    g.dfs()
    topolist = sorted(g.get_vertices(), 
                      key=lambda k: cast(Vertex, g.get_vertex(k)).get_closing_time(), 
                      reverse=True)
    return (topolist)

# This is the main function.
def main(args: list[str]) -> int:
    g = build_CS_Requirements()
    assert len(g.get_vertices()) == 16
    assert len(g.get_edges()) == 14
    print_graph(g)
    print (topologicalsort(g))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# My work is based on the explanation from class by Dr. Peter Brown.