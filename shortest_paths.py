# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:29:50 2015

@author: evanyao, robertchen, rak, anie
"""

import graph 
import data_structures as ds

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
           self.data_strucutre = ds.Priority()      

class ShortestPathsAStar(ShortestPathsAlg): 
    pass

