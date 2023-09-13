from pythonds3.graphs.adjacency_graph import Graph, Vertex
from typing import cast

#Incomplete Lesson from Dr. Brown

def build_7_18_graph() -> Graph:
    edges = [('A', 'B'), ('B', 'C'), ('B', 'E'), ('C', 'C'), ('C', 'F'),
             ('D', 'B'), ('D', 'G'), ('E', 'A'), ('E', 'D'), ('F', 'H'), 
             ('G', 'E'), ('H', 'I'), ('I', 'F')]
    g = Graph()
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    return g

def print_graph(g: Graph) -> None:
    for key in sorted(g.get_vertices()):
        vertex: Vertex = cast(Vertex, g.get_vertex(key))
        print(vertex, end='| ')
        for neighbor in vertex.get_neighbors():
            print(neighbor.get_key(), vertex.get_neighbor(neighbor), end='; ')
        print()
    print()

def transpose(g: Graph) -> Graph:
    """Create and return a graph gT that is the transpose of the given graph g.
    Assume that g is completely connected."""
    gT = Graph()
    for edge in g.get_edges():
        gT.add_edge(edge[1], edge[0])

    # Post (should catch if g or gT isn't completely connected)
    assert len(gT.get_vertices()) == len(g.get_vertices()) \
        and len(gT.get_edges()) == len(g.get_edges())
    return gT

def scc_dfs(g: Graph, gT: Graph) -> None:
    """Specialized DFS for strongly-connected components.  This DFS
    sorts the vertices of gT in decreasing order of closing time in g."""
    for key in sorted(g.get_vertices(), 
                      key=lambda k: cast(Vertex, g.get_vertex(k)).get_closing_time(),
                      reverse=True):
        gT_vertex = cast(Vertex, gT.get_vertex(key))
        if gT_vertex.get_color() == "white":
            gT.dfs_visit(gT_vertex)

def main(args: list[str]) -> int:
    g = build_7_18_graph()
    assert len(g.get_vertices()) == 9
    assert len(g.get_edges()) == 13
    print_graph(g)

    # Run a DFS on the initial graph
    g.dfs()
    print_graph(g)

    # Construct the transpose of the initial graph
    gT = transpose(g)
    assert len(gT.get_vertices()) == 9
    assert len(gT.get_edges()) == 13
    print_graph(gT)

    # Run a specialized DFS on gT, sorting the vertices in gT in decreasing
    # order of closing time in g.
    scc_dfs(g, gT)
    print_graph(gT)

    # The specialized DFS produces a forest; each strongly-connected
    # component is a tree in that forest.
    # FILL IN

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))