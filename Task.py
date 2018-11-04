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
        Time for release
        Node list
    """
    def __init__(self, ID, time, nodes):
        """ Initialise task with Node: time dictionary.
        """
        self.ID = ID
        self.time = time
        self.nodes = OrderedDict(nodes)
        self.cost = 0
        
    def getID(self):
        """ Return ID.
        """
        return self.ID
    
    def getTime(self):
        """ Return time step to release job.
        """
        return self.time
    