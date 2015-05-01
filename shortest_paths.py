# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:29:50 2015

@author: evanyao, robertchen, rak, anie
"""
 
import data_structures as ds
    
class ShortestPathsDijkstra:
    ''' 
    Shortest Paths via Dijkstra's 
    '''
    
    ''' 
    Given two stations, remembers the shortest path between them 
    if it was calculated previously" 
    '''
    # priority queue
    data_structure = None
    # stores previous node on shortest path between source and sink
    prev_array = []
    # shortest distance between source and sink
    dist_array = []
    num_stations = 0
    # adjacency matrix
    adj_list = []
    
    # extract graph instance variables 
    def __init__(self, graph, name, d = None):
       self.num_stations = graph.num_stations
       self.prev_array = [[None]*self.num_stations]*self.num_stations
       self.dist_array = [[float("inf")]*self.num_stations]*self.num_stations
       self.adj_list = graph.adj_list
       if name == 'heap' and d != None:
           self.ds = ds.DaryHeap(graph, d) 
       elif name == 'priority':
           self.ds = ds.Priority(graph)
       else:
           print "usage: ShortestPathDijkstra(graph, data_struct[, d-ary])"
    # Dijkstra's
    def singleSourceDist(self, init):
        # wavefront for testing
        self.ds.insert(init,0)
        # stores final distances behind wavefront
        dist = [float("inf")] * self.num_stations
        # stores whether a node has been searched
        searched = [False] * self.num_stations
        searched[init] = True
        # contains penultimate node on shortest path between source and sink
        prev = [None] * self.num_stations
        dist[init] = 0
        
        # priority queue depletes only once all accessible nodes are searched 
        while len(self.ds.data_structure) > 0:
            min_adj, dist[min_adj] = self.ds.deleteMin()
            for j,k in self.adj_list[min_adj].iteritems():
                test_dist = k + dist[min_adj]
                # find new nodes to search
                if not searched[j]:
                    searched[j] = True
                    self.ds.insert(j, test_dist)
                    prev[j] = min_adj
                    dist[j] = test_dist
                # found a better path
                elif dist[j] > test_dist:
                    prev[j] = min_adj
                    dist[j] = test_dist
                    self.ds.decreaseKey(j, test_dist)
        # store data from this run
        self.prev_array[init] = prev
        self.dist_array[init] = dist
                        
    def allDist(self):
        for i in range(0, self.num_stations):
            self.singleSourceDist(i)
    
    def extract_path(self, init, dest):
        path = []
        to_node = init
        # trace path through prev-array
        while to_node != dest:
            # inaccessible node
            if to_node == None:
                path = []
                break
            path.append(to_node)
            to_node = self.prev_array[dest][to_node]
        path.append(dest)
        return self.dist_array[init][dest], path
