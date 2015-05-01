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
    prev_array = []
    dist_array = []
    
    # extract graph instance variables 
    def __init__(self, graph, name, d = None):
       super(ShortestPathsDijkstra, self).__init__()
       self.prev_array = [[None]*self.num_stations]*self.num_stations
       self.dist_array = [[sys.maxint]*self.num_stations]*self.num_stations
       if name == 'heap' and d != None:
           self.data_structure = ds.Heap() 
       elif name == 'priority':
           self.data_structure = ds.Priority(d)
       else:
           print "usage: ShortestPathDijkstra(graph, data_struct[, d-ary])"
   
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
                    prev[j] = min_adj
                    dist[j] = test_dist
                elif dist[j] > test_dist:
                    prev[j] = min_adj
                    dist[j] = test_dist
                    self.data_structure.decreaseKey(j, test_dist)
        # prev list complete
        self.prev_array[init] = prev
        self.dist_array[init] = dist
                        
    def allDist(self):
        for i in range(0, self.num_stations):
            self.singleSourceDist(i)
        
    def extact_path(self, init, dest):
        path = []
        to_node = init
        while to_node != dest:
            paths.append(to_node)
            to_node = self.prev_array[dest][init]
        path.append[dest]
        return self.dist_array[init][dest], path
        
class ShortestPathsAStar(ShortestPathsAlg): 
    pass

congestion = ShortestPathsAlg
