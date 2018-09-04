# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:53:16 2018

@author: decka
"""

class Car:
    """ Represents a car in the warehouse that will travel between nodes along links.
    Attributes:
        Number (ID)
        Current Charge
        Current Location/Direction
        Current State

    State(int):
            0 = Charging
            1 = Idling
            2 = Moving
            3 = At goods/picking node
    """
    def __init__(self, ID):
        self.ID = ID
        self.state = 1
        self.task = None
        self.currentNode = None
        self.x = 0
        self.y = 0

    def addTask(self, task):
        self.task = task
        self.currentNode = list(task.nodes.items())[0] #Gives (ID, queue)
        self.state = 2

    def getID(self):
        return self.ID

    def getLocation(self):
        return self.x, self.y
    
    def setLocation(self, xNew, yNew):
        self.x = xNew
        self.y = yNew
    
    def progressTask(self):
        pass
    
    def moveToward(self, node):
        goalx, goaly = node.getPos()

        if (self.x == goalx) & (self.y == goaly):
            #Now at node
            self.state = 3
            print("Car", self.ID, "is already at Node", node.getID()+".")
            
        if (abs(self.x - goalx) > abs(self.y - goaly)):
            #Move in x dimension, further to go
            if(self.x > goalx):
                self.setLocation(self.x - 1, self.y)
                print("Car", self.ID, "moved left. New position:", self.getLocation())
            if(self.x < goalx):
                self.setLocation(self.x + 1, self.y)
                print("Car", self.ID, "moved right. New position:", self.getLocation())
                
        elif (abs(self.x - goalx) < abs(self.y - goaly)):
            #Move in y dimension, further to go
            if(self.y > goaly):
                self.setLocation(self.x, self.y - 1)
                print("Car", self.ID, "moved down. New position:", self.getLocation())
            if(self.y < goaly):
                self.setLocation(self.x, self.y + 1)
                print("Car", self.ID, "moved up. New position:", self.getLocation())
                
        elif (abs(self.x - goalx) == abs(self.y - goaly)):
            #Even distance, move x
            if(self.x > goalx):
                self.setLocation(self.x - 1, self.y)
                print("Car", self.ID, "moved left. New position:", self.getLocation())
            if(self.x < goalx):
                self.setLocation(self.x + 1, self.y)
                print("Car", self.ID, "moved right. New position:", self.getLocation())
                
        if (self.x == goalx) & (self.y == goaly):
            #Now at node
            self.state = 3
            print("Car", self.ID, "is now at Node", node.getID()+".")
            node.addCar(self, 1)