# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:30:03 2015

@author: Annie
"""
from graph import Graph
boston = Graph("BostonData.csv")
from final_a_star import a_star
   

def call_a_star(name1,name2):
    try:
        return a_star(boston,boston.get_number(name1),boston.get_number(name2))
    except TypeError:
        return "Typed name wrong!" 
