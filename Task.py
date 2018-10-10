# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:53:01 2018

@author: Declan Kavanagh
"""

from collections import OrderedDict

class Task:
    """ Represents a warehouse job.
    Attributes:
        Task ID
        Node list
    """
    def __init__(self, time, nodes):
        self.time = time
        self.nodes = OrderedDict(nodes)
        self.cost = 0
        

    def getTime(self):
        return self.time