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
    
def my_version(graph,starting_index,ending_index):
    return graph.a_star(starting_index,ending_index,False,testing=True)
   
N=30
"""Number of nodes in test graph """


for i in range(20):
    random_graph = gen_random_adj_matrix(N)
    test_graph = Graph(random_graph,None)
    print float(my_version(test_graph,1,9))==test_version(test_graph,1,9)

    
    