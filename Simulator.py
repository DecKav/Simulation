# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:51:18 2018

@author: Declan Kavanagh
"""

from Node import Node, Goods, Charger, Picker
from Task import Task
from Car import Car
from collections import OrderedDict
import math


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
        self.totalEnergy = 0
        self.moveCost = -5
        self.idleCost = -3
        self.nodeCost = -3
        self.chargeCost = 2
        self.taskEnergy = 0
        self.totalCost = 0
        root = Node(0,0)
        self.nodes[root.getID()] = root

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

    def addTask(self, time, nodes):
        taskAdd = Task(time, nodes)
        self.tasks[taskAdd.getTime()] = taskAdd
        print("Job at time step", taskAdd.getTime(), "created.")
        
    def addTaskSet(self, tasks):
        for time, task in tasks.items():
            pass                

    def timeStep(self, thresh1, thresh2):
        self.time = self.time + 1
        print("Step Number:", self.time)   
        print("======")
        
        self.totalEnergy = 0
        self.totalCost = 0
        
        """
        
        """
        
        #Iterate through tasks to establish current waiting cost
        for time, task in self.tasks.items():
            if(time <= self.time):
                prevNode = "00"
                for node in task.nodes:
                    currentNode = node
                    x1 = self.nodes[currentNode].getPos()[0]
                    x2 = self.nodes[prevNode].getPos()[0]
                    y1 = self.nodes[currentNode].getPos()[1]
                    y2 = self.nodes[prevNode].getPos()[1]
                    distance = abs(round(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0))
                    nodeTimeCost = task.nodes[node]*self.nodeCost*-1
                    moveTimeCost = distance*self.moveCost*-1
                    self.totalCost = self.totalCost + nodeTimeCost + moveTimeCost
                    prevNode = currentNode
            
        #Iterate through idling cars
        for car in self.cars:
            self.totalEnergy = self.totalEnergy + self.cars[car].getCharge()
            if self.cars[car].state == 1:
                if (self.tasks) and (self.cars[car].getCharge() > thresh1):
                    for key in self.tasks:
                        if(key <= self.time):
                            self.cars[car].addTask(self.tasks.pop(key))
                            break
                elif (self.cars[car].getCharge() < thresh2):
                    #Individual and Fleet threshold
                    self.cars[car].state = 0
                    print("Car", self.cars[car].getID(), "is now moving to be charged.")
                else:
                    self.cars[car].state = 1
        
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
                    if(currentCar.moveTowardCharge(self.chargers["13"])==True):
                        currentCar.changeCharge(self.chargeCost)
                    else:
                        currentCar.changeCharge(self.moveCost)
                elif currentCar.state == 1: # If car state is 'idling'
                    if(currentCar.moveTowardPoint(0, 0)==False):
                        currentCar.changeCharge(self.idleCost)
                    else:
                        currentCar.changeCharge(self.moveCost)                    
                elif currentCar.state == 2: # If car state is 'moving'
                    currentCar.moveToward(self.nodes[currentCar.getCurrentNodeID()])
                    currentCar.changeCharge(self.moveCost)
                elif currentCar.state == 3: # If car state is 'at node'
                    currentCar.changeCharge(self.nodeCost)
            print("Car "+str(currentCar.getID())+" Charge: "+str(currentCar.getCharge())+"%")
            
            
        ##Change in energy
        print("======")
        delta = 0
        for car in self.cars:
            delta = delta + self.cars[car].getCharge()
        
        deltaE = delta - self.totalEnergy 
        print("Total Energy at start:", str(self.totalEnergy))
        print("Average Energy at start:", str(self.totalEnergy/len(self.cars)))
        print("Energy Change in this step:", str(deltaE))
        
        self.totalEnergy = delta
        
        print("======")
        print("Current Job Queue Cost: "+str(self.totalCost))
               
        
        
        print("\n")
        
        for car in self.cars:
            currentCar = self.cars[car]
            if currentCar.state == 2:
                return False
            if currentCar.state == 3:
                return False
        
        if not self.tasks:
            print("TERMINATE")
            print(self.tasks.items)
            return True
        
        return False