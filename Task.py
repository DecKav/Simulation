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
        Start and finish nodes
        Deadline time to be completed by
    """
    def __init__(self, ID, nodes):
        self.ID = ID
        self.nodes = OrderedDict(nodes)

    def getStart(self):
        return self.start

    def getFinish(self):
        return self.finish

    def getID(self):
        return self.ID