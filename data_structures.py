# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:23:56 2015

@author: evanyao, robertchen, rak, anie
"""

class DijkstraDataStructure:
    ''' 
    Underlying Data structure for Dijkstra's Algorithm 
    ''' 
    def __init__(self, graph): 
        self.name = "Default List Dijkstra's" 
        self.data_structure = [] 
        
    def deleteMin(self): 
        pass 
    
    def decreaseKey(self, key, new_value): 
        pass 
    
    def insert(self, key, value): 
        pass

class Priority(DijkstraDataStructure): 
    ''' 
    Priority Queue in List form for Dijkstra's 
    '''
    pass 

class Heap(DijkstraDataStructure): 
    '''
    Binary Heap for Dijkstra's Algorithm
    '''
    pass

class Fib(DijkstraDataStructure):
    ''' 
    Fibonacci Heap for Dijkstra's Algorithm
    '''
    pass