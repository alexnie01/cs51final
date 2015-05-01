# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:23:56 2015

@author: evanyao, robertchen, rak, anie
"""
import math
import sys

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
        if len(self.data_structure) == 0:
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
        self.data_structure.insert(new_position, (key, value))
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
    def __init__(self, graph, d = 2):
        DijkstraDataStructure.__init__(self,graph)
        self.name = "Binary Heap Dijkstra's"
        self.d = d
    # swap two elements of the data structure and update their indices
    def swap(self, ind1, ind2):
        print "Swapping ", ind1, " and ", ind2
        temp = self.data_structure[ind1]
        self.data_structure[ind1] = self.data_structure[ind2]
        self.data_structure[ind2] = temp
        
    # compares child to parent in case child needs to swap with parent    
    def push_up(self, position):
        print "pushing up. indices are ", self.indices
        if position == 0:
            print "trivial push"
            return
        key, value = self.data_structure[position]
        parent = self.data_structure[(position-1)//self.d]  
        print "starting value and parent value are ", value, parent[1]
        print "position is ", position
        
        while value < parent[1] and position != 0:
            self.swap(position, (position-1)//self.d)
            self.indices[parent[0]] = position
            print "altered index of ", parent[0], " to ", position
            position = (position-1)//self.d
            self.indices[key] = position
            print "altered index of ", key, " to ", position
            print "after swapping with parents, indices are ", self.indices
            parent = self.data_structure[(position-1)//self.d]
            
    def insert(self, key, value):
        node = (key, value)
        position = len(self.data_structure)
        print "Inserting ", node
        print "before inserting, indices are ", self.indices
        self.data_structure.append(node)
        print "key is ", key
        self.indices[key] = position
        print "before pushing key, indices are now ", self.indices
        self.push_up(position)
        print "Heap is now ", self.data_structure
        print "after pushing key, indices are now ", self.indices
    # pops minimum value from heap and rebalances        
    def deleteMin(self):
        length = len(self.data_structure)
        print "Called deleteMin with length ", length
        print "heap is ", self.data_structure
        if length == 0:
            return None
            # if our heap was initially empty, should fail
        self.swap(0,-1)
        
        min_node = self.data_structure.pop()
        length -= 1
        self.indices[min_node[0]] = None
        print "after pulling ", min_node[0], "indices are ", self.indices
        print "min_node was ", min_node
        position = 0
        print "heap has length ", len(self.data_structure)
        if length == 0:
            self.indices[min_node[0]] = None
            return min_node
        print "                  REBALANCING                      "
        # log condition checks if node has reached bottom branch
        while position == 0 or int(math.log(length, self.d)) - int(math.log(position + 1, self.d)) > 0:
            best_child = None
            best_child_value = sys.maxint
            search = (length - 1)%self.d
            if search == 0 and length > 0:
                search = self.d
            print "search is ", search
            for i in range(1, search + 1):
                print "position, d, i", position, self.d, i
                print "next position to be tested is ", self.d * position + i
                print "length is ", length
                print "self.data_structure is currently ", self.data_structure
                if self.d * position + i >= length:
                    break
                test_value = self.data_structure[self.d * position + i][1]
                if test_value < min(self.data_structure[position][1], 
                                    best_child_value):
                    best_child = self.d * position + i
                    best_child_value = test_value
            if best_child != None:
                print "Decided best child was ", self.data_structure[best_child], " at index ", best_child
                self.indices[self.data_structure[best_child][0]] = position
                self.swap(position, best_child)
                position = best_child
                self.indices[self.data_structure[position][0]] = position
                print "heap is ", self.data_structure
                print "self.indices is \n", self.indices
            else:
                print "no best child found. heap is ", self.data_structure
                self.indices[self.data_structure[position][0]] = position
                return min_node
        print "reached end of heap"
        self.indices[self.data_structure[position][0]] = position
        return min_node
    def decreaseKey(self, key, new_value):
        print "decreaseKey called on (", key, ", ", new_value, ")"
        position = self.indices[key]
        print "Position is ", position
        print "self.data_structure is ", self.data_structure
        # if node has been bumped out of queue then must redo search process to
        # also adjust adjacent node distances
        if position == None:
            self.insert(key, new_value)
            return
        if new_value < self.data_structure[position][1]:
            self.data_structure[position] = (key, new_value)
            self.push_up(position)