# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:29:50 2015

@author: evanyao, robertchen, rak, anie
"""

import graph 
import data_structures as ds
import final_a_star.a_star as a_star 

''' 
Abstract Class for Shortest Path Algorithms to implemenet

'''
class ShortestPathsAlg(graph.Graph): 
    ''' 
    Returns the shortest path to every other station as well 
    as their corresponding total weight
    '''
    def singleSourceDist(self, init): 
        pass
    
    ''' 
    Populates the paths_lookup dictionary completely 
    '''
    def allDist(self): 
        pass 


    
class ShortestPathsDijkstra(ShortestPathsAlg):
    ''' 
    Shortest Paths via Dijkstra's 
    '''
    
    ''' 
    Given two stations, remembers the shortest path between them 
    if it was calculated previously" 
    '''
    paths_lookup = {} 
    
    def __init__(self, name):
       super(ShortestPathsDijkstra, self).__init__()   
       if name == 'heap': 
           self.data_structure = ds.Heap() 
       elif name == 'fib': 
           self.data_structure = ds.Fib()
       else: 
           self.data_structure = ds.Priority()  
   
   '''
   Init = initial node index
   '''
   def singleSourceDist(self, init):
       
       # wavefront
       self.data_structure.insert(init,0)
       
       # stores final distances behind wavefront
       dist = [sys.maxint] * self.num_stations
       
       # contains penultimate node on shortest path between source and sink
       prev = [None] * self.num_stations
       dist[init] = 0
            
        while len(self.data_structure) > 0:
            
            min_adj, dist[min_adj] = self.data_structure.deleteMin()
            searched[min_adj] = True
            
            for j,k in self.adj_list[min_adj].iteritems():
                test_dist = k + dist[min_adj]
                if not searched[j]:
                    self.data_structure.insert(j, test_dist)
                elif dist[j] > test_dist:
                    dist[j] = test_dist
                    self.data_structure.decreaseKey(j, test_dist)
        # compile paths
                        
    def allDist(self):
        return None

class ShortestPathsAStar(ShortestPathsAlg): 
    pass

congestion = ShortestPathsAlg
