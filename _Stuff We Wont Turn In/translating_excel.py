# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:08:09 2015

@author: Annie
"""

import pandas
import csv

colnames = ['number', 'name']
data = pandas.read_csv('paris_ids.csv', names=colnames)

dct=data.set_index('number').to_dict()
dct = dct['name']
del dct['number']

edges = pandas.read_csv('paris_edges.csv', names=colnames)

edges = edges.as_matrix()
edges= edges.tolist()

for i in range(len(edges)):
    edges[i][0]=dct[str(edges[i][0])]
    edges[i][1]=dct[str(edges[i][1])]
    
with open('named_edges.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(edges)