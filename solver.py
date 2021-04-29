import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob


def solve(G):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(15, num_edges)
    c_constraint = 1

    nodes_removed = 0
    edges_removed = 0

    while nodes_removed < c and edges_removed < k:
        try:
            shortest_st_path = nx.dijkstra_path(G,0,num_nodes-1)
        except nx.NetworkXNoPath:
            break
    
    # small graphs c = 1, not considering edges
    list of nodes

    while True:
        get shortest path
        construct subgraph
        find min cut nodes to disconnect
        if cardinality of min cut nodes <= c and original graph is not disconnected:
            store min cut nodes
        else:
            store previous best
            break
    while True:
        get shortest path
        
    
    # process edges next
    





    


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     c, k = solve(G)
#     assert is_valid_solution(G, c, k)
#     print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
#     write_output_file(G, c, k, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('inputs/*')
#     for input_path in inputs:
#         output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G = read_input_file(input_path)
#         c, k = solve(G)
#         assert is_valid_solution(G, c, k)
#         distance = calculate_score(G, c, k)
#         write_output_file(G, c, k, output_path)
