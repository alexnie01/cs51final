# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:48:07 2015

@author: Alexander
"""

from scipy.sparse.csgraph import shortest_path 
from scipy.stats import bernoulli
import numpy as np
import itertools
#Create a random adjacency matrix

from graph import Graph

def gen_random_adj_matrix(N):
    b = np.random.random_integers(0,2000,size=(N,N))
    b_symm = (b + b.T)/2    
    p = 0.6    
    for i,j in itertools.combinations(range(N),2):
        if (bernoulli.rvs(p,1)-1):
            b_symm[i][j]=0
            b_symm[j][i]=0
    return b_symm

        
def test_version(graph,starting_index,ending_index):
    adj_matrix = graph.adj_matrix   
    solution = shortest_path(adj_matrix,directed=False)
    return solution[starting_index][ending_index]
    
def my_version(graph, init, dest, struct, d, namedList = False, testing = True):
    return graph.dijkstra(init, dest, struct, d, namedList, testing)
"""Number of nodes in test graph """

if __name__ == "__main__":    
    N = 50
    tests = 20
    struct = 'priority'
    
    for i in range(0, tests):
        d = np.random.randint(2,6)
        init = np.random.randint(0,N)
        dest = np.random.randint(0,N)        
        random_graph = gen_random_adj_matrix(N)
        test_graph = Graph(random_graph, None)
        a = test_version(test_graph, init, dest)
        b = float(my_version(test_graph, init, dest, struct, d, testing = True))
        assert(a==b)
        print "success!"

    
    