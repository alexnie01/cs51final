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
        # tracks index of key in data_structure
        self.indices = [None] * self.num_stations
        
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
    def deleteMin(self):
        self.data_structure.pop(0)
        # update index trackers
        length = len(self.indices)
        for i in range(0,length):
            if self.indices[i] != None:
                self.indices -= 1
    # performs insertion sort with new node    
    def insert(self, key, value):
        node = (key, value)
        if len(self.data_structure = 0):
            self.data_structure.append(node)
            self.indices[key] = 0
        else:
            self.data_structure.append(node)
            self.push_up(len(self.data_structure))
            
    def push_up(self, position):
        key, value = self.data_structure[position]
        new_position = position
        while new_position > -1 and value <= self.data_structure[new_position - 1][1]:
            self.indices[self.data_structure[new_position - 1][0]] += 1
            new_position -= 1
        self.data_structure.pop(position)
        self.data_structure.insert(new_postion, (key, value))
        self.indices[key] = new_position
            
    def decreaseKey(self, key, new_value):
        position = self.indices[key]
        if new_value < self.data_structure[position][1]:
            self.data_structure[position] = (key, new_value)
            self.push_up(position)
            
class DaryHeap(DijkstraDataStructure): 
    '''
    Dary Heap for Dijkstra's Algorithm
    '''
    def __init__(self, graph, d):
        super(BinaryHeap, self).__init__(graph)
        self.name = "Binary Heap Dijkstra's"
        self.d = d
    # swap two elements of the data structure and update their indices
    def swap(self, ind1, ind2):
        temp = self.data_structure[ind1]
        self.data_structure[ind1] = self.data_structure[ind2]
        self.data_structure[ind2] = temp
        
    # compares child to parent in case child needs to swap with parent    
    def push_up(self, position):
        key, value = self.data_structure[position]
        parent = self.data_structure[position//self.d]  
        
        while value < parent[1]:
            self.swap(position, position//self.d)
            self.indices[parent[0]] = position
            position //= self.d
            self.indices[key] = position
            parent = self.data_structure[position//self.d]
            
    def insert(self, key, value):
        node = (key, value)
        position = len(self.data_structure)
        self.data_structure.append(node)
        self.push_up(position)
            
    def deleteMin(self):
        length = len(self.data_structure)
        if length == 0:
            return None
        self.swap(0,-1)
        min_node = self.data_structure.pop()
        position = 0
        # log condition checks if node has reached bottom branch, 
        while int(math.log(length,d)) - int(math.log(position,d)) > 0:
            best_child = None
            best_child_value = sys.maxint
            for i in range(0,d):
                test_value = self.data_structure[d * position + i][1]
                if test_value < min(self.data_structure[position][1], 
                                    best_child_value):
                    best_child = d * position + i
                    best_child_value = test_value
            if best_child != None:
                self.swap(position, best_child)
                self.indices[self.data_structure[best_child][0]] = position
                position = best_child
                self.indices[min_node[0]] = position
            return min_node
    def decreaseKey(self, key, new_value):
        position = self.indices[key]
        if new_value < self.data_structure[position][1]:
            self.data_structure[position] = (key, new_value)
            self.push_up(position)