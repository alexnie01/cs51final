# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:29:50 2015

@author: evanyao, robertchen, rak, anie
"""
 
import data_structures as ds
import sys
from pprint import pprint
    
class ShortestPathsDijkstra:
    ''' 
    Shortest Paths via Dijkstra's 
    '''
    
    ''' 
    Given two stations, remembers the shortest path between them 
    if it was calculated previously" 
    '''
    data_structure = None
    prev_array = []
    dist_array = []
    num_stations = 0
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
    def singleSourceDist(self, init):
        print "------------------START------------------\n\n"
        print "starting on ", init
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
        while len(self.ds.data_structure) > 0:   
            print "------------Step-------------"
            min_adj, dist[min_adj] = self.ds.deleteMin()
            print "pulled ", min_adj, " from list"
            print "adjacent nodes are"
            pprint(self.adj_list[min_adj])
            for j,k in self.adj_list[min_adj].iteritems():
                test_dist = k + dist[min_adj]
                if not searched[j]:
                    print j, " previously not searched. Inserting into heap."
                    searched[j] = True
                    self.ds.insert(j, test_dist)
                    prev[j] = min_adj
                    dist[j] = test_dist
                elif dist[j] > test_dist:
                    print j, "was searched, but a shorter path exists. decreasing key."
                    prev[j] = min_adj
                    dist[j] = test_dist
                    self.ds.decreaseKey(j, test_dist)
        self.prev_array[init] = prev
        print "prev array is now ", self.prev_array[init]
        self.dist_array[init] = dist
        print "dist array is now ", self.dist_array[init]
                        
    def allDist(self):
        for i in range(0, self.num_stations):
            self.singleSourceDist(i)
        print "adjacency list is "
        pprint(self.adj_list)
        print "prev array is now ", 
        pprint(self.prev_array)
        print "dist array is now "
        pprint(self.dist_array)
    def extract_path(self, init, dest):
        print "extracting path between ", init, " and ", dest
        print "prev_array is "
        pprint(self.prev_array)
        path = []
        to_node = init
        while to_node != dest:
            if to_node == None:
                path = []
                break
            path.append(to_node)
            print "dest is ", dest, " and init is ", init
            to_node = self.prev_array[dest][to_node]
            print "path is currently ", path
            print "to_node is currently ", to_node
        path.append(dest)
        print "path is ", path
        return self.dist_array[init][dest], path
