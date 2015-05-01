# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:09:37 2015

@author: Annie
"""

from scipy.sparse.csgraph import shortest_path 
from scipy.stats import bernoulli
import numpy as np
import itertools
#Create a random adjacency matrix

from a_star_test_version import a_star

class Graph_test:
    adj_matrix = []
    def get_neighbors(self,horizon_index):
        return [i for i,v in enumerate(self.adj_matrix[horizon_index]) if v > 0]   
    def get_distance(self,vertex_i,vertex_j):
        solution = shortest_path(self.adj_matrix,directed=False)
        return (float(solution[vertex_i][vertex_j]))/2
    def path_length(self, node_list): 
        if len(node_list)==0:
            return 0
        cumul_distance=0
        for i in range(0,len(node_list)-1):
            distance=self.adj_matrix[node_list[i]][node_list[i+1]]
            cumul_distance=cumul_distance+distance
        return cumul_distance

    def __init__(self, N):
        b = np.random.random_integers(0,2000,size=(N,N))
        b_symm = (b + b.T)/2    
        p = 0.6    
        for i,j in itertools.combinations(range(N),2):
            if (bernoulli.rvs(p,1)-1):
                b_symm[i][j]=0
                b_symm[j][i]=0
        self.adj_matrix = b_symm
    
        
def test_version(graph,starting_index,ending_index):
    adj_matrix = graph.adj_matrix   
    solution = shortest_path(adj_matrix,directed=False)
    return solution[starting_index][ending_index]
    
def my_version(graph,starting_index,ending_index):
    return a_star(graph,starting_index,ending_index)
    
for i in range(10):
    test_graph = Graph_test(20)
    print float(my_version(test_graph,1,9))==test_version(test_graph,1,9)

    
    