# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:32:14 2015

@author: Annie
"""

import networkx as nx
import Orange

test=Orange.network.readwrite.read_pajek('Paris-2009-adjacency.net')
paris_directed=nx.read_pajek('Paris-2009-adjacency.net')

paris_undirected = nx.Graph()

for u,v,data in paris_directed.edges_iter(data=True):
    w = data['weight']
    if paris_undirected.has_edge(u,v):
        paris_undirected[u][v]['weight'] += w
    else:
        paris_undirected.add_edge(u, v, weight=w)
        
paris_undirected
