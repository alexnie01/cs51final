# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:23:56 2015

@author: evanyao, robertchen, rak, anie
"""
import math

class DijkstraDataStructure:
    ''' 
    Underlying Data structure for Dijkstra's Algorithm 
    ''' 
    name = ""
    data_structure = []
    indices = []
    
    def __init__(self, graph): 
        self.name = "Default List Dijkstra's" 
        # tracks index of key in data_structure
        self.indices = [None] * graph.num_stations
        
    def deleteMin(self): 
        pass  
        
    def insert(self, key, value): 
        pass
    
    def decreaseKey(self, key, new_value):
        position = self.indices[key]
        # if node has been bumped out of queue then must redo search process to
        # also adjust adjacent node distances
        if position == None:
            self.insert(key, new_value)
            return
        if new_value < self.data_structure[position][1]:
            self.data_structure[position] = (key, new_value)
            self.push_up(position)
class Priority(DijkstraDataStructure): 
    ''' 
    Priority Queue in List form for Dijkstra's 
    '''
    def deleteMin(self):
        node = self.data_structure.pop(0)
        # update index trackers
        length = len(self.indices)
        for i in range(0,length):
            if self.indices[i] != None:
                self.indices[i] -= 1
        self.indices[node[0]] = None
        return node
    # performs insertion sort with new node    
    def insert(self, key, value):
        node = (key, value)
        length = len(self.data_structure)
        if length == 0:
            self.data_structure.append(node)
            self.indices[key] = 0
        else:
            self.data_structure.append(node)
            self.indices[key] = length
            self.push_up(length)
    # rebalancing method
    def push_up(self, position):
        key, value = self.data_structure[position]
        new_position = 0
        # find smallest node greater than our pushed node
        for new_position in range(0, position):
            if value <= self.data_structure[new_position][1]:
                break
        # update indices of nodes between our new and old position
        for i in range(new_position, position):
            self.indices[self.data_structure[i][0]] += 1
        self.data_structure.pop(position)
        self.data_structure.insert(new_position, (key,value))
        self.indices[key] = new_position
    
class DaryHeap(DijkstraDataStructure): 
    '''
    d-ary Heap for Dijkstra's Algorithm
    '''
    def __init__(self, graph, d = 2):
        DijkstraDataStructure.__init__(self,graph)
        self.name = "d-ary Heap Dijkstra's"
        self.d = d
    # swap two elements of the priority queue
    def swap(self, ind1, ind2):
        temp = self.data_structure[ind1]
        self.data_structure[ind1] = self.data_structure[ind2]
        self.data_structure[ind2] = temp
        
    # compares child to parent in case child needs to swap with parent    
    def push_up(self, position):
        if position == 0:
            return
        key, value = self.data_structure[position]
        parent = self.data_structure[(position-1)//self.d]
        while value < parent[1] and position != 0:
            self.swap(position, (position-1)//self.d)
            self.indices[parent[0]] = position
            position = (position-1)//self.d
            self.indices[key] = position
            parent = self.data_structure[(position-1)//self.d]
            
    def insert(self, key, value):
        node = (key, value)
        position = len(self.data_structure)        
        self.data_structure.append(node)        
        self.indices[key] = position
        self.push_up(position)
    def deleteMin(self):
        length = len(self.data_structure)
        if length == 0:
            return None
        self.swap(0,-1)        
        min_node = self.data_structure.pop()
        length -= 1
        self.indices[min_node[0]] = None
        position = 0
        if length == 0:
            return min_node
        # log condition checks if node has reached bottom level of heap
        while position == 0 or int(math.log(length, self.d)) - int(math.log(position + 1, self.d)) > 0:
            # determine child with smallest value
            best_child = None
            best_child_value = float("inf")
            search = (length - 1)%self.d
            if search == 0 and length > 0:
                search = self.d
            for i in range(1, search + 1):
                if self.d * position + i >= length:
                    break
                test_value = self.data_structure[self.d * position + i][1]
                if test_value < min(self.data_structure[position][1], 
                                    best_child_value):
                    best_child = self.d * position + i
                    best_child_value = test_value
            # if needed, swap with smallest child
            if best_child != None:
                self.indices[self.data_structure[best_child][0]] = position
                self.swap(position, best_child)
                position = best_child
                self.indices[self.data_structure[position][0]] = position
            else:
                self.indices[self.data_structure[position][0]] = position
                return min_node
        self.indices[self.data_structure[position][0]] = position
        return min_node