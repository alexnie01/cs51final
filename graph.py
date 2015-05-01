# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:29:51 2015

@authors: evanyao, robertchen, rak, anie
"""

'''
Format for input CSV file: see the sample file.
'''

'''
Graph's variables: 
adj_list: list of dictionaries of int keys and int values

adj_matrix: list of lists of ints

station_lookup: list of dictionaries with various info

index_lookup: dictionary of string keys and int values

num_stations: int

Graph's methods:

__compute_distance(position1, position2) [intended to be private]

__readInput(file_name) [intended to be private]

__init__(file_name) [intended to be private]

get_names()

print_summary()

add_station(name, usage, neighbors, position)

add_route(station1, station2)

    delete_route(station1, station2)
'''

import csv
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt 
import itertools
from collections import Counter
from scipy.sparse import csr_matrix
from final_a_star import a_star as imported_a_star

"""FOR THE SAKE OF PROVIDING HEURISTIC FOR TESTING SHORTEST PATH ON 
RANDOM ADJACENCEY MATRICES. NOT CHEATING"""
from scipy.sparse.csgraph import shortest_path 


class Graph:
    ''' 
    A class that stores the map of a transportation network as an 
    undirected graph. 
    '''  
    # Adjacency List representation of our graph for quick neighbors
    #List of dictionaries. Key is which vertex the edge connects to. Value is edge weight.
    #Example: [{1: 3, 2: 5, 3: 4, 4: 1}, {0: 3, 3: 2, 4: 3}, {0: 5, 3: 2}, {0: 4, 1: 2, 2: 2, 4: 4}, {0: 1, 1: 3, 3: 4}]
    adj_list = []
    
    testing = False
    
    #Adjacency Matrix representation of our graph for quick lookups
    #List of lists of integers. Entries are 0 if those two vertices don't have an edge between them, else entry is edge weight.
    #Example: [[0, 3, 5, 4], [3, 0, 0, 2], [5, 0, 0, 2], [4, 2, 2, 0]]
    adj_matrix = []
    
    def adj_matrix_to_list(self,adjacency_matrix):
        adj_list = []        
        for i in range(len(adjacency_matrix)):
            neighbors = [j for j, e in enumerate(adjacency_matrix[i]) if e != 0]
            neighbor_values =  filter(lambda b: b >0, adjacency_matrix[i])
            dct = dict(zip(neighbors,neighbor_values))
            adj_list.append(dct)
        return adj_list
    
    # List of dictionaries allows us to lookup station information by index, such as station name, usage rate, coordinates
    #Example: [{'Usage': 50, 'Index': 0, 'Name': 'Harvard', 'Position': (0, 0)}, {'Usage': 20, 'Index': 1,
    #'Name': 'Central', 'Position': (0, 2)}, {'Usage': 90, 'Index': 2, 'Name': 'Park Street', 'Position': (0, 4)},
    #{'Usage': 35, 'Index': 3, 'Name': 'Logan Airport', 'Position': (1, 3)}]
    station_lookup = [] 
    
    # Dictionary allows us to lookup station's index using the station's name
    #Example: {'Logan Airport': 3, 'Harvard': 0, 'Central': 1, 'Park Street': 2}
    index_lookup = {}
    
    # Number of stations in the network 
    num_stations = 0 
    
    graph_obj = nx.Graph()
    
    '''
    Computes Cartesian distance (edge weight) given coordinate positions of two stations. Rounds up by taking floor and adding
    1. Edge weight is always at least 1.
    '''
    def compute_distance (self, position1, position2):
        x1 = float(position1[0])
        x2 = float(position1[1])
        y1 = float(position2[0])
        y2 = float(position2[1])
        dist = np.floor(np.sqrt(((x1 - y1)*(x1 - y1)) + ((x2 - y2)*(x2 - y2)))) + 1.0
        
        return (int(dist))
    
    def get_distance(self,node1,node2):
        if self.testing:
            solution = shortest_path(self.adj_matrix,directed=False)
            return (float(solution[node1][node2]))/2
        else:
            position1 = self.station_lookup[node1]['Position']
            position2 = self.station_lookup[node2]['Position']
            return self.compute_distance(position1,position2)
        
    def path_length(self, node_list): 
        if len(node_list)==0:
            return 0
        cumul_distance=0
        for i in range(0,len(node_list)-1):
            distance=self.adj_matrix[node_list[i]][node_list[i+1]]
            cumul_distance=cumul_distance+distance
        return cumul_distance
        
    def nums_to_names(self,index_list):
        return [self.station_lookup[num]['Name'] for num in index_list]
    
    ''' 
    Reads the graph in from a file and populates the instance 
    variables accordingly 
    
    Returns 5 variables: an adjacency list, adjacency matrix, station lookup list, index lookup dictionary, number of stations
    ''' 
    def __readInput(self, file_name): 
        
        #Open csv file for reading.
        with open(file_name, 'rU') as fh:
    
            subway_csv = csv.reader(fh, delimiter=',', quotechar='"')

            initialAdjList = []
            initialAdjMatrix = []
            initialStationLookup = []
            initialIndexLookup = {}
            initialNumStations = 0

            #To keep track of what row in the csv currently being read.
            counter = (-1)
            
            #Skip header row
            next(subway_csv, None)

            for row in subway_csv:

                #Read first row of csv file.
                if counter == (-1):
                    initialNumStations = int(row[0])

                    #Initialize initialAdjMatrix with 0s and initialAdjList list with proper length.
                    for i in range(initialNumStations):
                        initialAdjMatrix.append(([0]*initialNumStations))
                        initialAdjList.append({})

                    #Initialize initialStationLookup list with proper length.
                    initialStationLookup = [{}]*initialNumStations

                #Read the rows of the csv files about single stations.
                elif counter < initialNumStations:
                    initialStationLookup[counter] = {"Index": counter, "Name": row[0], "Usage": int(row[1]),"Position": (int(row[2]), int(row[3]))}
                    initialIndexLookup[row[0]] = counter

                #Read the rows of the csv files about edges between stations.
                else:
                    #Add edge weight to initialAdjMatrix and initialAdjList
                    index1 = initialIndexLookup[row[0]]
                    index2 = initialIndexLookup[row[1]] 
                    #Compute the edge weight based on station positions.
                    new_weight = self.compute_distance(initialStationLookup[index1]["Position"], initialStationLookup[index2]["Position"])
                    
                    initialAdjMatrix[index1][index2] = new_weight
                    initialAdjMatrix[index2][index1] = new_weight
                    initialAdjList[index1][index2] = new_weight
                    initialAdjList[index2][index1] = new_weight

                counter = counter + 1
        
        return (initialAdjList, initialAdjMatrix, initialStationLookup, initialIndexLookup, initialNumStations)
    
    '''
    Constructor
    '''
    def __init__(self,adj_matrix=None,file_name=None): 
        if adj_matrix== None:        
            self.adj_list, self.adj_matrix, self.station_lookup, self.index_lookup, \
            self.num_stations = self.__readInput(file_name)
            self.initializeGraph()
        else :
            self.adj_matrix=adj_matrix
            self.adj_list = self.adj_matrix_to_list(self.adj_matrix)
            self.graph_obj = nx.from_scipy_sparse_matrix(csr_matrix(adj_matrix))
            self.num_stations = len(adj_matrix)
            self.testing = True
            
            
    def a_star(self,start_index,end_index,named_list,testing):
        return imported_a_star(self,start_index,end_index,named_list,self.testing)
        
    ''' 
    Returns an array where indices are station indices and values are names 
    '''
    def get_number(self,station_name):
        for station in self.station_lookup:
            if station["Name"]==station_name:
                return station['Index']
        return 'No station with that exactly phrased name.'
    
    def get_names(self): 
        all_names = []
        for station in self.station_lookup:
            all_names.append(station["Name"])
        return all_names
    
    ''' 
    Prints out information about the graph  
    '''
    def print_summary(self): 
        print "Information about this Graph:"
        print
        print "Number of Stations: "
        print self.num_stations
        print
        print "Station Indices by Station Name: "
        print self.index_lookup
        print
        print "Station Info by Station Index: "
        for entry in self.station_lookup:
            print entry
        print
        print "Adjacency Matrix: "
        for entry in self.adj_matrix:
            print entry
        print
        print "Adjacency List: "
        for entry in self.adj_list:
            print entry
    
    ''' 
    Given a new station name, its usage, coordinates, a list of its neighbors by name,
    we add it into the adjacency list and matrix representations
    '''
    def add_station(self, name, usage, neighbors, position): 
        
        #Update station_lookup
        self.station_lookup.append({"Index": self.num_stations, "Name":name, "Usage":usage, "Position":position})
        
        #Update index_lookup
        self.index_lookup[name] = self.num_stations
        
        #Update adj_matrix and adj_list
        
        #First change the sizes of adj_matrix and adj_list
        for lst in self.adj_matrix:
            lst.append(0)
        self.adj_matrix.append([0] * (self.num_stations + 1))
        
        self.adj_list.append({})
        
        self.graph_obj.add_node(self.num_stations)
        
        #Now input the edges
        for i in range(len(neighbors)):
            otherindex = self.index_lookup[neighbors[i]]
            
            #Compute edge weight based on station positions.
            new_weight = self.compute_distance(self.station_lookup[otherindex]["Position"], self.station_lookup[self.num_stations]["Position"])
            
            self.graph_obj.add_edge(otherindex, self.num_stations)            
            
            self.adj_matrix[otherindex][self.num_stations] = new_weight
            self.adj_matrix[self.num_stations][otherindex] = new_weight
            
            self.adj_list[otherindex][self.num_stations] = new_weight
            self.adj_list[self.num_stations][otherindex] = new_weight               
                      
        #Update num_stations
        self.num_stations = self.num_stations + 1
            
    ''' 
    Adds an edge to the graph, given two station names that are already in the graph. Overwrites old edge weight if there
    was already an edge.
    ''' 
    def add_route(self, station1, station2): 
        index1 = self.index_lookup[station1]
        index2 = self.index_lookup[station2]
        
        weight = self.compute_distance(self.station_lookup[index1]["Position"], self.station_lookup[index2]["Position"])
        
        self.adj_matrix[index1][index2] = weight
        self.adj_matrix[index2][index1] = weight
        self.adj_list[index1][index2] = weight
        self.adj_list[index2][index1] = weight
        
        self.graph_obj.add_edge(index1, index2)
        
    ''' 
    Delete an edge of the graph, given two station names that are already in the graph. Does nothing is an edge is already
    not present.
    ''' 
    def delete_route(self, station1, station2): 
        index1 = self.index_lookup[station1]
        index2 = self.index_lookup[station2]
        self.adj_matrix[index1][index2] = 0
        self.adj_matrix[index2][index1] = 0
        del self.adj_list[index1][index2]
        del self.adj_list[index2][index1]
        self.graph_obj.remove_edge(index1, index2)
    
    def initializeGraph(self): 
        self.graph_obj.add_nodes_from(range(self.num_stations))
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] != 0: 
                    self.graph_obj.add_edge(i,j, weight = self.adj_matrix[i][j])
    
    def calculateCongestion(self): 
        cong = Counter()
        for (one, two) in list(itertools.combinations(range(self.num_stations), 2)): 
            one_pop = self.station_lookup[one]['Usage'] 
            two_pop = self.station_lookup[one]['Usage'] 
            path = self.a_star(one, two,False,False) 
            for p in range(len(path) - 1): 
                cong[(min(path[p], path[p+1]) , max(path[p], path[p+1]))] += (min([one_pop,two_pop]))
        
        # normalizing the congestions to be between 0 and 1 
        maximum = max(cong.values())     
        
        for key in cong.keys(): 
            cong[key] /= float(maximum)
            
        self.congestion = cong  
        
    def draw(self, colorCalculation, congestion = True, recalculate = False):
        
        pos={} 
        for i in range(self.num_stations): 
            pos[i] = self.station_lookup[i]['Position']        
            
        if not congestion: 
            nx.draw(self.graph_obj, pos, node_size = 15) 
            return 
            
        if recalculate or not hasattr(self, 'congestion'): 
            self.calculateCongestion() 
        

            
        # Colorful nodes representing the total usage of that station 
        for i in range(len(self.station_lookup)): 
            usage = self.station_lookup[i]['Usage']
            color = [usage/23000., np.sqrt(usage/23000.), 1 - usage/23000.]
            nx.draw_networkx_nodes(self.graph_obj, pos, nodelist = [i], node_color = [color], node_size = 30,with_labels=False)
#            nx.draw_networkx_labels(self,pos,labels = [i],font_size=1000)

        for i in range(len(self.adj_list)): 
            for j in self.adj_list[i].keys(): 
                x = min(i,j) 
                y = max(i,j)
                c = self.congestion[(x,y)]
                nx.draw_networkx_edges(self.graph_obj, pos, edgelist = [(x,y)], edge_color = [colorCalculation(c)], width = 4)
#%% 
                
def main():
    subway = Graph(None,'BostonData.csv')               
    #%%               
    def color(c): 
        return [ 1 - (1-c) ** 10, 0.8, 0.3]   
    
    subway.draw(color)
    
    plt.savefig("path.png") # save as png
    plt.title("Boston Subway System")
    plt.show()

    #%%
def f():
    return []   
paris=Graph(None,'paris_orig.csv')
paris.draw(f,False)
plt.savefig("paris.pdf")
plt.show()

nx.draw(paris.graph_obj)