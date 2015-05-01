# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:42:19 2015

@author: Annie
"""
import itertools
#import time

#from graph import Graph

#def path_length(graph, node_numbers): #NODE NAMES IS A LIST OF THE NODES IN A PATH
#    if len(node_numbers)==0:
#        return 0
#    cumul_distance=0
#    for i in range(0,len(node_numbers)-1):
#        distance=graph.adj_matrix[node_numbers[i]][node_numbers[i+1]]
#        cumul_distance=cumul_distance+distance
#    return cumul_distance


def nums_to_names(agenda,graph):
    return [graph.station_lookup[num]['Name'] for num in agenda]

def a_star(graph, start, goal):
    if start==goal:
        return([start])  
        
    agenda=[[start]]
    
    while len(agenda)!=0:   
        frontpath=agenda[0]
        if goal in frontpath:
            return graph.path_length(frontpath)

#EXTEND THE FRONT PATH            
        horizon_index = frontpath[-1]
        neighbors=graph.get_neighbors(horizon_index)
        replacement=[]
        for neighbor in neighbors:
#IF IT DOES NOT DO SOMEWHERE IT ALREADY WENT
            if neighbor not in frontpath:
                bud=list(frontpath)
                bud.append(neighbor)
                replacement.append(bud)

#REPLACE THE FRONT PATH WITH THE PATHS EXTENDING OUT OF IT           
        agenda.pop(0)
        agenda=replacement+agenda
#SEE IF ANY TWO PATHS IN AGENDA OF PATHS END AT THE SAME PLACE AND PICK THE SHORTER OF THE TWO
        to_drop = []        
        for i,j in itertools.combinations(range(len(agenda)),2):
            if agenda[i]==agenda[j]:
                to_drop.append(agenda[i])
        for drop in to_drop:
            agenda.remove(drop)
        to_drop = []
        for i,j in itertools.combinations(range(len(agenda)),2):
            if agenda[i][-1]==agenda[j][-1]:
                if graph.path_length(agenda[i])>graph.path_length(agenda[j]):
                    to_drop.append(agenda[i])
                else:
                    to_drop.append(agenda[j])
        for drop in to_drop:
            agenda.remove(drop)
      
                    
#SORT ALL PATHS ONLY ACCORDING TO PATH LENGTH AND HEURISTIC VALUE      
        lengths_plus_heuristic=[]

        for path in agenda:           
            length=graph.path_length(path)
            node=path[-1]
            heuristic=graph.get_distance(node,goal)
            lengths_plus_heuristic.append(length+heuristic)        

#THIS IS A FUNCTION TO UNIQUIFY A LIST
        def f10(seq, idfun=None): # Andrew Dalke
            # Order preserving
            return list(_f10(seq, idfun))
        
        def _f10(seq, idfun=None):
            seen = set()
            if idfun is None:
                for x in seq:
                    if x in seen:
                        continue
                    seen.add(x)
                    yield x
            else:
                for x in seq:
                    x = idfun(x)
                    if x in seen:
                        continue
                    seen.add(x)
                    yield x    
        
        sorted_lengths_plus_heuristic = f10(sorted(lengths_plus_heuristic))
        sorted_agenda = []        

        for i in range(len(sorted_lengths_plus_heuristic)):
            for j in range(len(agenda)):
                if lengths_plus_heuristic[j]==sorted_lengths_plus_heuristic[i]:
                    sorted_agenda.append(agenda[j])      
        agenda=sorted_agenda          
    return []
    
