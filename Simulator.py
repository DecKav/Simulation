# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:51:18 2018

@author: Declan Kavanagh
"""

from Node import Node, Goods, Charger, Picker
from Task import Task
from Car import Car
from collections import OrderedDict

class Simulator:
    """ Controls all nodes, links, and cars. Advances time, manages job list.

    Attributes:
        Node list
        Car list
        Task list
        Time steps taken
    """
    def __init__(self):
        self.nodes = {}
        self.chargers = {}
        self.cars = {}
        self.tasks = OrderedDict()
        self.time = 0
        self.taskCount = 0
        self.totalEnergy = 0;

    def addNode(self, x, y):
        nodeAdd = Node(x,y)
        self.nodes[nodeAdd.getID()] = nodeAdd
        print("Node", nodeAdd.getID(), "created.")
        
    def addCharger(self, x, y):
        nodeAdd = Charger(x,y)
        self.chargers[nodeAdd.getID()] = nodeAdd
        print("Charger", nodeAdd.getID(), "created.")

    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.getID()] = carAdd
        print("Car", carAdd.getID(), "created.")

    def addTask(self, nodes):
        self.taskCount = self.taskCount + 1
        ID = self.taskCount
        taskAdd = Task(ID, nodes)
        self.tasks[taskAdd.getID()] = taskAdd
        print("Job number", taskAdd.getID(), "created.")
                

    def timeStep(self):
        self.time = self.time + 1
        print("Step Number:", self.time)
        
        
        
        #Iterate through idling cars
        for car in self.cars:
            if self.cars[car].state == 1:
                if (self.tasks) and (self.cars[car].getCharge() > 25):
                    self.cars[car].addTask(self.tasks.popitem(False)[1])
                elif (self.cars[car].getCharge() < 50):
                    #Individual and Fleet threshold
                    self.cars[car].state = 0
                    print("Car", self.cars[car].getID(), "is now moving to be charged.")
        
        #Iterate through all node queues
        totalClear = []
        for node in self.nodes:
            carClear = []
            currentNode = self.nodes[node]
            for car in currentNode.queue: 
                #Decrease time of each car at node
                currentNode.queue[car] = currentNode.queue[car] - 1
                if currentNode.queue[car] == 0:
                    #Remove from queue
                    carClear.append(car)
                    totalClear.append(car)
                else:
                    print("Car", car.getID(), "is at Node", currentNode.getID(), "for", currentNode.queue[car], "more time steps.")
            if carClear:
                for car in carClear:
                    self.nodes[node].removeCar(car)
                    car.state = 2
                    car.progressTask()
                            
                    
        # Iterate through every car, update charge
        for car in self.cars:
            currentCar = self.cars[car]
            if currentCar not in totalClear:
                if currentCar.state == 0: # If car state is 'charging'
                    if(currentCar.moveTowardCharge(self.chargers["22"])==True):
                        currentCar.changeCharge(10)
                elif currentCar.state == 1: # If car state is 'idling'
                    if(currentCar.moveTowardPoint(0, 0)==False):
                        currentCar.changeCharge(-5)
                    else:
                        currentCar.changeCharge(-10)                    
                elif currentCar.state == 2: # If car state is 'moving'
                    currentCar.moveToward(self.nodes[currentCar.getCurrentNodeID()])
                    currentCar.changeCharge(-10)
                elif currentCar.state == 3: # If car state is 'at node'
                    currentCar.changeCharge(-5)
            print("Car "+str(currentCar.getID())+" Charge: "+str(currentCar.getCharge())+"%")
            
        ##Change in energy
        
               
        
        
        print("\n")