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
    '''
    def decreaseKey(self, key, new_value): 
        pass 
    '''
    def insert(self, key, value): 
        pass

class Priority(DijkstraDataStructure): 
    ''' 
    Priority Queue in List form for Dijkstra's 
    '''
    def deleteMin(self):
        self.data_structure.pop(0)
    # performs insertion sort with new node    
    def insert(self, key, value):
        node = {"key":key, "value":value}
        if len(self.data_structure = 0):
            self.data_structure.append(node)
        else:
            length = len(self.data_structure)
            for i in range(0, length):
                if value < self.data_structure[i]["value"]:
                    self.data_structure.insert(i,node)
                    return
                elif value == self.data_structure[i]["value"]:
                    self.data_structure[ind][key] = value
                    return
            self.data_structure.append(node)
            
class BinaryHeap(DijkstraDataStructure): 
    '''
    Binary Heap for Dijkstra's Algorithm
    '''
    def __init__(self,graph):
        super(BinaryHeap, self).__init__(graph)
        self.name = "Binary Heap Dijkstra's"
        
    # swap two elements of the data structure
    def swap(self, ind1, ind2):
        temp = self.data_structure[ind1]
        self.data_structure[ind1] = self.data_structure[ind2]
        self.data_structure[ind2] = temp
    # pushes inserted node up the tree. note that the old length becomes
    # the index of the new node on first call
    def upper(self, ind):

        par = ind%2 == 0
        
        while ind//2 > 0:
            # takes care of two cases in which we need to perform parent-child
            # swapping: greater left-child and smaller right-child
            if self.data_structure[ind]["value"] > self.data_structure[ind//2]["value"] != par:
                self.swap(ind, ind//2)
                ind//=2
                par = ind%2 == 0
            else:
                break
        self.downer(ind)
         
    def downer(self, ind):
        while ind < len(self.data_structure):
            if self.data_structure[ind]["value"] <= self.data_structure[2 * ind]["value"]:
                self.swap(ind, 2*ind)
                ind *= 2
            elif self.data_structure[ind]["value"] >= self.data_structure[2 * ind + 1]["value"]:
                self.swap(ind, 2 * ind + 1)
                ind = 2 * ind + 1
            else:
                break
            
    def insert(self, key, value):
        length = len(self.data_structure)
        if length == 0:
            self.data_structure.append({"key":key, "value":value, "left":None, "right":None})
        else:
            node = {key:value}
            self.data_structure.append(node)
            self.upper(length)
            
class Fib(DijkstraDataStructure):
    ''' 
    Fibonacci Heap for Dijkstra's Algorithm
    '''
    pass