import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob
import random


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

    removed_edge = False
    last_edge = None

    H = G.copy()

    shortest_path = nx.dijkstra_path(H, 0, num_nodes - 1)
    #print(shortest_path)
    num_edges = len(shortest_path) - 1
    #print("Num edges:", num_edges)
    index = 0
    while not removed_edge:
        try:
            sorted_edges = sorted( [(shortest_path[i], shortest_path[i+1]) for i in range(0,len(shortest_path) - 1)], key = (lambda e : H.edges[e[0],e[1]]['weight']) , reverse=True)
            last_edge = sorted_edges[index]
            H.remove_edge(*last_edge)

            if nx.has_path(H, 0, num_nodes - 1):
                return [], [last_edge]
            else:
                index += 1

        except nx.NetworkXNoPath:
            print("No path from source to target node")
        except Exception as e:
            print("Last edge:", last_edge)
            print(e)
            break
    return [],[]
    # while nodes_removed < c and edges_removed < k:
    #     try:
    #         shortest_st_path = nx.dijkstra_path(G,0,num_nodes-1)
    #     except nx.NetworkXNoPath:
    #         break
    
    # # small graphs c = 1, not considering edges
    # list of nodes

    # while True:
    #     get shortest path
    #     construct subgraph
    #     find min cut nodes to disconnect
    #     if cardinality of min cut nodes <= c and original graph is not disconnected:
    #         store min cut nodes
    #     else:
    #         store previous best
    #         break
    # while True:
    #     get shortest path


def min_cut_solve(G):
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(100, num_edges)
    c_constraint = 5

    # H = G.copy() # edited copy of graph
    S = nx.Graph()

    rem_nodes = []
    H = G.copy()
    control = nx.dijkstra_path(G, 0, num_nodes - 1)
    # print(H.edges)

    while True:
        try:
            shortest_path = nx.dijkstra_path(H, 0, num_nodes - 1)
        except nx.NetworkXNoPath:
            break
        #print(shortest_path == control)
        S.add_weighted_edges_from([(x, y, G.edges[x,y]["weight"]) for x,y in nx.utils.pairwise(shortest_path)])
        #print(S.edges)
        nodes = nx.algorithms.connectivity.minimum_st_node_cut(S,0,num_nodes - 1)
        #print(len(nodes))
        if len(nodes) > c_constraint:
            break
        # edit H
        elif len(nodes) == 0:
            break
        else:
            H.remove_nodes_from(nodes)
            if nx.is_connected(H):
                rem_nodes = nodes
            else:
                break

    I = G.copy()
    I.remove_nodes_from(rem_nodes)       

    #calculate_score(H,c,rem_edges)     
    
    rem_edges = []
    while len(rem_edges) < k_constraint:
        try:
            shortest_path = nx.dijkstra_path(I, 0, num_nodes - 1)
        except nx.NetworkXNoPath:
            if rem_edges:
                del rem_edges[-1]
            break
        count = 5
        while count > 0:
            edge = random.choice(list(nx.utils.pairwise(shortest_path)))
            K = I.copy()
            K.remove_edge(*edge)
            if nx.is_connected(K) and nx.has_path(K,0,num_nodes-1):
                I.remove_edge(*edge)
                rem_edges.append(edge)
                break
            count -= 1
        # min edge in shortest path



        # heuristic logic
        # maxScore = float('-inf')
        # edge = None
        # for x,y in nx.utils.pairwise(shortest_path):
        #     curr_score = calculate_score(I, [], [(x,y)])
        #     if curr_score > maxScore:
        #         maxScore = curr_score
        #         edge = (x,y)
        # if edge:
        #     rem_edges.append(edge)
        #     I.remove_edge(*edge)
        # else:
        #     break
    
    # try:
    #     shortest_path = nx.dijkstra_path(I, 0, num_nodes - 1)
    # except nx.NetworkXNoPath:

    # if not I.has_path(0,num_nodes-1):
    #     del rem_edges[-1]

    
    return rem_nodes, rem_edges
        

        # if not shortest_path:
        #     break
        # S.add_weighted_edges_from([(x, y, G[x,y]["weight"]) for x,y in nx.utils.pairwise(shortest_path)])
        # nodes = nx.algorithms.connectivity.minimum_st_edges_cut(S,0,num_nodes - 1)
        # if len(nodes) > c_constraint:
        #     break
        # # edit H
        # else:
        #     H.remove_nodes_from(nodes)
        #     if nx.is_connected(H):
        #         rem_nodes = nodes
        #     else:
        #         break
                
    # random step 


        # S.add_edge(a,b, weight = n)
        # nx.utils.pairwise(shortest_path)
        # S.edges[a,b]["weight"]

        
    
    # process edges next
    

# keep track of a list of shortest paths + costs
# keep track of weighted out-degree of a node




    


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2 
    path = sys.argv[1]
    G = read_input_file(path)
    c, k = min_cut_solve(G)
    print(c,k)
    assert is_valid_solution(G, c, k)
    print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
    write_output_file(G, c, k, 'outputs/large-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     size = ["small", "medium", "large"]
#     for s in size:
#         # dir_path = 
#         inputs = glob.glob(f"inputs/{s}/*")
#         # print(dir_path, inputs)
#         for input_path in inputs:
#             output_path = f'outputs/{s}/' + basename(normpath(input_path))[:-3] + '.out'
#             G = read_input_file(input_path)
#             c, k = solve(G)
#             assert is_valid_solution(G, c, k)
#             distance = calculate_score(G, c, k)
#             write_output_file(G, c, k, output_path)
