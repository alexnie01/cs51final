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
    '''
    d = None
    N = input("How many nodes would you like to test?")
    tests = input("How many tests would you like to run?")
    struct = raw_input("Store as naive list ('priority') or binary heap ('heap')?")
    if struct == 'heap':
        d = input("How many children per node?")
    init = input("Index to start at?")
    dest = input("Destination index?")
    '''
    d = 3
    N = 7
    tests = 1
    struct = 'heap'
    init = 1
    dest = 6
    
    for i in range(0, tests):
        random_graph = gen_random_adj_matrix(N)
        test_graph = Graph(random_graph, None)
        a = test_version(test_graph, init, dest)
        b = float(my_version(test_graph, init, dest, struct, d, testing = True))
        print "a is ", a, ". b is ", b
        print a == b

    
    