from pythonds3.graphs.adjacency_graph import Graph, Vertex
from typing import cast

def build_knights_tour(dim: int) -> Graph:
    # Pre:
    assert dim > 2
    rows: list[int] = list(range(1, dim+1)) # rows in [1, dim]
    cols: list[str] = [chr(i) for i in range(ord('a'), ord('a') + dim)]
    print (rows, cols)
    g = Graph()

    moves: list[tuple[int, int]] = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                                    (2, -1), (2, 1), (1, -2), (1, 2)]
    # Add the knight's moves on the board
    for r in rows:
        for c_num in range(1, dim+1): # Column number
            for move in moves:
                if 0 < (r + move[0]) <= dim and 0 < (c_num + move[1]) <= dim:
                    g.add_edge(cols[c_num-1] + str(r), 
                               cols[c_num - 1 + move[1]] + str(r + move[0]))
    return g

def print_graph(g: Graph) -> None:
    for key in sorted(g.get_vertices()):
        vertex: Vertex = cast(Vertex, g.get_vertex(key))
        print(vertex, end='| ')
        for neighbor in vertex.get_neighbors():
            print(neighbor.get_key(), vertex.get_neighbor(neighbor), end='; ')
        print()

def knights_tour(depth: int, current: Vertex | None, next: Vertex, limit: int) -> bool:
    done = False
    if current is not None:
        print(depth, current.get_key(), next.get_key())
    if depth == limit:
        done = True
    elif next.get_color() != 'white':
        done = False
    else:  # next.get_color() == white
        next.set_previous(cast(Vertex, current))
        next.set_color('gray')

        for neighbor in sorted(next.get_neighbors(), key=lambda v: len(v.get_neighbors())):
            done = knights_tour(depth + 1, next, neighbor, limit)
            if done:
                break
        if not done: # next doesn't work.  Prepare to backtrack.
            next.set_color('white')
            next.set_previous(cast(Vertex, None))
    return done

def print_tour(start: Vertex, limit: int) -> None:
    print('Tour:', end=" ")
    current = start
    depth = 1
    while depth < limit:
        depth = depth + 1 #Increase even if we don't find a neighbor (i.e., the last vertex)
        print(current.get_key(), end=' ')
        oldcurrent = current
        # Find the next node in the list
        for neighbor in current.get_neighbors():
            #assert neighbor != current
            if neighbor.get_previous() == current:
                current = neighbor
                break
        #assert current != oldcurrent
    print(current.get_key())

def main(args: list[str]) -> int:
    dimension = 5
    g = build_knights_tour(dimension)
    assert len(g.get_vertices()) == (dimension**2)
    #assert len(g.get_edges()) == 336
    print_graph(g)
    if knights_tour(0, None, cast(Vertex, g.get_vertex('a1')), dimension**2):
        print("Path found.")
        print_tour(cast(Vertex, g.get_vertex('a1')), dimension**2)
    else:
        print('Path not found.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))