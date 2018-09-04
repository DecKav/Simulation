# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:52:32 2018

@author: decka
"""

class Node:
    """ Represents a node in a warehouse that cars need to move between.
    Attributes:
        ID = str(xy)
        Location [x,y]
        Queue (car times)
    """
    def __init__(self, x, y):
        self.ID = str(x)+str(y)
        self.x = x
        self.y = y
        self.queue = {}

    def addCar(self, Car, time):
        self.queue[Car] = time
        print("Car", Car.getID(), "added to", self.ID+".")

    def removeCar(self, Car):
        del self.queue[Car]
        print("Car", Car.getID(), "removed from", self.ID+".")

    def getID(self):
        return self.ID

    def getPos(self):
        return self.x, self.y



class Goods(Node):
    """ Represents a node in a warehouse that cars will retrieve and store goods at.
    Inherits from Node.
    Attributes:
        Goods
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)


class Picker(Node):
    """ Represents a node in a warehouse that cars will transport goods to.
    Inherits from Node.
    Attriubutes:
        Working Order
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)


class Charger(Node):
    """ Represents a node in a warehouse that cars will be charged at.
    Inherits from Node.
    Attributes:
        Charge Rate
        Car Queue
    """
    def __init__(self, x, y):
        Node.__init__(self, x, y)