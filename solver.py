import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob
import random
from itertools import islice
from collections import defaultdict

def solve(G,a,b):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(a, num_edges)
    c_constraint = b

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


def min_cut_solve(G,a,b):
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(a, num_edges)
    c_constraint = b

    # H = G.copy() # edited copy of graph
    S = nx.Graph()

    rem_nodes = []
    H = G.copy()
    control = nx.dijkstra_path(G, 0, num_nodes - 1)
    # print(H.edges)

    while True:
        # print("LOL")
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
    prev_path = []
        

    while len(rem_edges) < k_constraint:
        # print("BYE")
        try:
            shortest_path = nx.dijkstra_path(I, 0, num_nodes - 1)
        except nx.NetworkXNoPath:
            if rem_edges:
                del rem_edges[-1]
            break
        if prev_path == shortest_path:
            break
        count = 5
        while count > 0:
            edge = random.choice(list(nx.utils.pairwise(shortest_path)))
            # print(count,edge)
            K = I.copy()
            K.remove_edge(*edge)
            if nx.is_connected(K) and nx.has_path(K,0,num_nodes-1):
                I.remove_edge(*edge)
                rem_edges.append(edge)
                break
            
            count -= 1
        prev_path = shortest_path
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


    


# k shortest paths
def get_k_shortest_path(G,S,edge_limit,node_limit):
    # takes in graph and returns list of k shortest paths
    num_nodes = nx.number_of_nodes(G)
    # num_edges = nx.number_of_edges(G)

    # k_constraint = min(edge_limit, num_edges)
    c_constraint = node_limit

    # Have to figure out how to choose k
    # n = n_val

    # shortest_paths = list(
    #     islice(nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight"), n)
    # )

    # compute a subgraph
    # S = nx.Graph()
    # for i in range(n):
    #     S.add_weighted_edges_from([(x, y, G.edges[x,y]["weight"]) for x,y in nx.utils.pairwise(shortest_paths[i])])
    
    # find min_edge cut + process adjacent nodes
    min_cut = nx.algorithms.connectivity.cuts.minimum_st_edge_cut(S, 0, num_nodes-1)

    nodes_in_cut = set()
    prev_edges = []
    for x,y in min_cut:
            nodes_in_cut.add(x)
            nodes_in_cut.add(y)
    if 0 in nodes_in_cut:
        nodes_in_cut.remove(0)
    if num_nodes-1 in nodes_in_cut:
        nodes_in_cut.remove(num_nodes-1)
    
    # sort node by degree
    sorted_nodes = sorted(list(G.degree(nodes_in_cut)), key = (lambda x : x[1]), reverse=True)

    # select nodes to remove in descending order
    nodes_removed = 0
    removed_nodes = set()
    for node,_ in sorted_nodes:
        I = G.copy()
        I.remove_node(node)
        if nx.is_connected(I) and nx.has_path(I,0,num_nodes-1): # jic
            removed_nodes.add(node)
            prev_edges = [edge for edge in min_cut if node in edge]
            nodes_removed += 1
        else:
            continue
        if nodes_removed == c_constraint:
            break

    return list(removed_nodes), prev_edges

def new_solve(G, edge_limit, node_limit):

    with open("results.txt", "w") as f:
        path_dict = defaultdict(int)

        num_nodes = nx.number_of_nodes(G)
        num_edges = nx.number_of_edges(G)

        k_constraint = min(edge_limit, num_edges)
        c_constraint = node_limit

        removed_nodes = []
        
        print("Beginning")
        path_generator = nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight")
        print("Between")
        path_list = list(path_generator)
        print(len(path_list))
        print("After")

        # path_generator = nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight")
        # S = nx.Graph()

        # print("Start")
        # print("---------------------------")

        # prev_edges = []
        # buffer = next(path_generator)

        # while True:
        #     #update subgraph
        #     next_path = buffer
        #     try:
        #         buffer = next(path_generator)
        #     except StopIteration:
        #         break
        #     # if not buffer:
        #     #     break
        #     print("next_path:", next_path)
        #     S.add_weighted_edges_from([(x, y, G.edges[x,y]["weight"]) for x,y in nx.utils.pairwise(next_path)])

        #     #get nodes for current subgraph
        #     returned_nodes, prev_edges = get_k_shortest_path(G,S,k_constraint,c_constraint)
        #     print("returned_nodes:", returned_nodes)
        #     print("prev_edges:", prev_edges)
        #     path_dict[str(prev_edges)] += 1
        #     #check for stop condition
        #     S_copy = S.copy()
        #     S_copy.remove_nodes_from(returned_nodes)

        #     if len(prev_edges) >= k_constraint:
        #         break
        #     else:
        #         print("else")
        #         if returned_nodes:
        #             removed_nodes = returned_nodes
        #         else:
        #             print("Returned_nodes is empty")
        #     f.write(str(path_dict))

        # # most recent S
        # G_minus_nodes = G.copy()
        # G_minus_nodes.remove_nodes_from(removed_nodes)

        # I = G_minus_nodes.copy()
        # removed_edges = []
        # for edge in prev_edges:
        #     I.remove_edge(*edge)
        #     if nx.is_connected(I) and nx.has_path(I,0,num_nodes-1):
        #         removed_edges.append(edge)
        #     else:
        #         continue
        
        # return removed_nodes, removed_edges
        return [],[]

def new_new_solve(G, edge_limit, node_limit):
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(edge_limit, num_edges)
    c_constraint = node_limit

    removed_nodes = []
    
    # print("Beginning")
    # path_generator = nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight")
    # print("Between")
    # path_list = list(path_generator)
    # print(len(path_list))
    # print("After")

    # path_generator = nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight")
    length = dict(nx.single_source_bellman_ford_path_length(G,0))
    neighbor_shortest_paths = nx.single_source_bellman_ford_path(G,0)
    shortest_paths = sorted([ n for n in G.neighbors(num_nodes - 1)], key=(lambda x : length[x] + G.edges[x,num_nodes - 1]["weight"]))
    S = nx.Graph()

    print("Start")
    print("---------------------------")

    index = 0
    prev_edges = []
    # buffer = next(path_generator)

    while True:
        #update subgraph
        if index >= len(shortest_paths):
            break
        next_path = neighbor_shortest_paths[shortest_paths[index]]
        index += 1

        # try:
        #     buffer = next(path_generator)
        # except StopIteration:
        #     break
        # if not buffer:
        #     break
        print("next_path:", next_path)
        S.add_weighted_edges_from([(x, y, G.edges[x,y]["weight"]) for x,y in nx.utils.pairwise(next_path)])

        #get nodes for current subgraph
        returned_nodes, prev_edges = get_k_shortest_path(G,S,k_constraint,c_constraint)
        print("returned_nodes:", returned_nodes)
        print("prev_edges:", prev_edges)
        # path_dict[str(prev_edges)] += 1
        #check for stop condition
        S_copy = S.copy()
        S_copy.remove_nodes_from(returned_nodes)

        if len(prev_edges) >= k_constraint:
            break
        else:
            print("else")
            if returned_nodes:
                removed_nodes = returned_nodes
            else:
                print("Returned_nodes is empty")
        # f.write(str(path_dict))

    # most recent S
    G_minus_nodes = G.copy()
    G_minus_nodes.remove_nodes_from(removed_nodes)

    I = G_minus_nodes.copy()
    removed_edges = []
    for edge in prev_edges:
        I.remove_edge(*edge)
        if nx.is_connected(I) and nx.has_path(I,0,num_nodes-1):
            removed_edges.append(edge)
        else:
            continue
    
    return removed_nodes, removed_edges 

# remove from min cut nodes
def remove_min_cut(G,edge_limit, node_limit):
    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)

    k_constraint = min(edge_limit, num_edges)
    c_constraint = node_limit

    removed_nodes = []

    # print("Beginning")
    path_generator = nx.shortest_simple_paths(G, 0, num_nodes-1, weight="weight")
    # print("Between")
    # path_list = list(path_generator)
    # print(len(path_list))
    # print("After")
    
    S = nx.Graph()
    removed_nodes = []

    while True:
        try:
            next_path = next(path_generator)
        except StopIteration:
            break
        S.add_weighted_edges_from([(x, y, G.edges[x,y]["weight"]) for x,y in nx.utils.pairwise(next_path)])
        returned_nodes = get_nodes(G,S,c_constraint)
        if returned_nodes:
            removed_nodes = returned_nodes
        else:
            break
    
    I = G.copy()
    I.remove_nodes_from(removed_nodes)

    removed_edges = []
    
    # while True:
    #     if len(removed_edges) >= k_constraint:
    #         break

    #     try:
    #         shortest_path = nx.dijkstra_path(I, 0, num_nodes - 1)
    #     except nx.NetworkXNoPath:
    #         break

    #     sorted_nodes = sorted(list(G.degree(shortest_path)), key = (lambda x : x[1]), reverse=True)
    #     edge = None

    #     for x in sorted_nodes:
    #         if x == 0 or x == num_nodes - 1:
    #             continue
    #         i = shortest_path.index(x)
    #         if G.edges[x,shortest_path[i+1]]["weight"] > G.edges[shortest_path[i-1], x]["weight"]:
    #             edge = (shortest_path[i-1], x)
    #         else:
    #             edge = (x, shortest_path[i+1])

    #         if edge:
    #             copy = I.copy()
    #             copy.remove_edge(*edge)
    #             if nx.is_connected(copy) and nx.has_path(copy, 0, num_nodes - 1):
    #                 removed_edges.append(edge)
    #                 break
    #         edge = None
        
    #     if not edge:
    #         break
    prev_path = None

    while len(removed_edges) < k_constraint:
        # print("BYE")
        try:
            shortest_path = nx.dijkstra_path(I, 0, num_nodes - 1)
        except nx.NetworkXNoPath:
            if removed_edges:
                del removed_edges[-1]
            break
        if prev_path == shortest_path:
            break
        count = 5
        while count > 0:
            edge = random.choice(list(nx.utils.pairwise(shortest_path)))
            # print(count,edge)
            K = I.copy()
            K.remove_edge(*edge)
            if nx.is_connected(K) and nx.has_path(K,0,num_nodes-1):
                I.remove_edge(*edge)
                removed_edges.append(edge)
                break
            
            count -= 1
        prev_path = shortest_path
      
    return removed_nodes, removed_edges

def get_nodes(G,S,node_limit):
    num_nodes = nx.number_of_nodes(G)

    min_cut = nx.algorithms.connectivity.cuts.minimum_st_node_cut(S, 0, num_nodes-1)

    if len(min_cut) <= node_limit:
        I = G.copy()
        I.remove_nodes_from(min_cut)
        if nx.is_connected(I) and nx.has_path(I, 0, num_nodes - 1):
            return min_cut
    
    return None

# def get_edges(G,S,node_limit, edge_limit):
#     num_nodes = nx.number_of_nodes(G)
#     min_cut = nx.algorithms.connectivity.cuts.minimum_st_edge_cut(S, 0, num_nodes-1)

#     if len(min_cut) <= edge_limit:
#         I = G.copy()
#         I.remove_nodes_from(min_cut)
#         if nx.is_connected(I) and nx.has_path(I, 0, num_nodes - 1):
#             return min_cut
    
#     return None
        
        
    
            





# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2 

    path = sys.argv[1]
    file_name = basename(normpath(path))[:-3]
    G = read_input_file(path)
    
    # c,k = new_solve(G,3,50)
    # c,k = min_cut_solve(G,50,3)
    max_c,max_k = remove_min_cut(G,50,3)
    max_score = calculate_score(G, max_c,max_k)
    # for i in range(1):
    #     c,k = remove_min_cut(G,50,3)
    #     score = calculate_score(G, c, k)
    #     print(f"Shortest Path Difference: {score}")
    #     if score > max_score:
    #         max_c, max_k = c, k
    #         max_score = score
    # print(max_c,max_k)
    # assert is_valid_solution(G, c, k)
    print("Best score:", max_score)
    write_output_file(G, max_c,max_k, f'outputs/small/{file_name}.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     # size = [("small",15,1), ("medium",50,3), ("large",100,5)]
#     size = [("medium",50,3)]
#     for s in size:
#         inputs = glob.glob(f"inputs/{s[0]}/*")
#         for input_path in inputs:
#             file_name = basename(normpath(input_path))[:-3]
#             print(file_name)
#             output_path = f'outputs/{s[0]}/' + file_name + '.out'
#             G = read_input_file(input_path)

#             # max_c,max_k = min_cut_solve(G,s[1],s[2])
#             max_c,max_k = remove_min_cut(G,s[1],s[2])
#             max_score = calculate_score(G, max_c, max_k)

#             for i in range(50):
#                 c,k = remove_min_cut(G,s[1],s[2])
#                 score = calculate_score(G, c, k)
#                 # print(f"Shortest Path Difference: {score}")
#                 if score > max_score:
#                     max_c, max_k = c, k
#                     max_score = score
#             c, k = min_cut_solve(G,s[1],s[2])
#             # assert is_valid_solution(G, c, k)
#             # distance = calculate_score(G, c, k)
#             print("Score for '", file_name, "':", max_score)
#             # print("Score for '", file_name, "':", distance)
#             write_output_file(G, max_c, max_k, output_path)
