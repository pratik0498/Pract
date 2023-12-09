"""
SNA practical 1: Write a program to compute the following for a given a network:
1) number of edge
2) number of nodes
3) degree of nodes
4)node with lowest degree,
5)the adjacency list
6)matrix of the graph
"""

import networkx as nx
import numpy as np

def compute_graph_properties(graph):
    
    # Number of edges
    num_edges = graph.number_of_edges()
    
    #Number of nodes
    num_nodes = graph.number_of_nodes()
    
    #Degree of nodes
    nodes_degrees = dict(graph.degree())
    
    #Node with lowest degree
    min_degree_node = min(nodes_degrees, key=nodes_degrees.get)
    
    #Adjacency List
    adjacency_list = dict(graph.adjacency())
    
    #Adjacency Matirx
    adjacency_matrix = nx.adjacency_matrix(graph).todense()
    
    return num_edges, num_nodes, nodes_degrees, min_degree_node, adjacency_matrix ,adjacency_matrix

#Eaxmple

G = nx.Graph()
G.add_edges_from([(1,4), (2,8), (3,6), (4,7), (5,3), (2,9), (7,6)])

#compute teh graph properties
edges, nodes, degrees, min_degree_node, adj_list, adj_matrix = compute_graph_properties(G)

#Display results
print("Number of edges:",edges)
print("Number of nodes:",nodes)
print("Degree of nodes:",degrees)
print("Mode with lowest degree:",min_degree_node)
print("Adjacency List:\n",adj_list)
print("Adjacency Matrix:\n",adj_matrix)
