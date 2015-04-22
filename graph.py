# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:29:51 2015

@authors: evanyao, robertchen, rak, anie
"""

class Graph:
    ''' 
    A class that stores the map of a transportation network as an 
    undirected graph. 
    '''  
    
    # Adjacency List representation of our graph for quick neighbors
    adj_list = []
    
    # Adjacnecy Matrix representation of our graph for quick lookups
    adj_matrix = [[]]
    
    # Allows us to lookup station names by their number 
    station_lookup = {} 
    
    # Looks up the edge weights indexd by a tuple 
    weight_lookup = {}
    
    # Number of stations in the network 
    num_stations = 0 
    
    ''' 
    Reads the graph in from a file and populates the instance 
    variables accordingly 
    
    Returns 4 variables: the adjacency list, matrix, station lookup, and weight lookup
    ''' 
    def __readInput(file_name): 
        pass
    
    ''' 
    Returns an array where indices are station id's and values are names 
    '''
    def __getNames(station_lookup): 
        pass
    
    def __init__(self, file_name): 
        self.adjacnecy_list, self.adjacency_matrix, self.station_lookup, \
        self.weight_lookup = self.__readInput(file_name) 
        
        self.names = self.__getNames(self.station_lookup)
        self.num_stations = len(self.adjancency_list)    
    
    ''' 
    Prints out some information about the graph 
    (if we have time) make it pretty 
    '''
    def __str__(self): 
        pass    
    
    ''' 
    Given a new station name, and a list of its neighbors, 
    we add it into the adjacency list and matrix representations
    '''
    def addStation(self, name, neighbors): 
        pass 
    
    ''' 
    Adds and edge to the graph, given two station ID's 
    ''' 
    def addPath(self, _from, _to): 
        pass 
    
    ''' 
    Returns whether or not every edge in this graph is undirected 
    
    NOTE: it will not require stations of the same name to have 
    only undirected edges between them. See 'splitNode()' below 
    ''' 
    def checkSymmetry(self): 
        pass
    
    ''' 
    Takes a node and makes it into 2 nodes with a directed edge of weight 
    'congestion' in between to symbolize the transfer or wait time 
    necessary at this station. Both nodes have the same station name 
    in the dictionary. 
    '''
    def splitNode(self, name, congestion):
        pass 