# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:51:18 2018

@author: decka
"""

from Node import Node
from Task import Task
from Car import Car

class Simulator:
    """ Controls all nodes, links, and cars. Advances time, manages job list.

    Attributes:
        Node list
        Link list
        Car list
        Task list
    """
    def __init__(self):
        self.nodes = {}
        self.cars = {}
        self.tasks = {}
        self.time = 0

    def addNode(self, x, y):
        nodeAdd = Node(x,y)
        self.nodes[nodeAdd.getID()] = nodeAdd
        print("Node", nodeAdd.getID(), "created.")

    def addCar(self, ID):
        carAdd = Car(ID)
        self.cars[carAdd.getID()] = carAdd
        print("Car", carAdd.getID(), "created.")

    def addTask(self, ID, nodes, duration, carID):
        taskAdd = Task(ID, nodes, duration)
        self.tasks[taskAdd.getID()] = taskAdd
        self.cars[carID].addTask(taskAdd)
        print("Job number", taskAdd.getID(), "created.")

    def timeStep(self):
        self.time = self.time + 1
        print("Step Number:", self.time)
        
        # Iterate through every car
        for car in self.cars:
            currentCar = self.cars[car]
            if currentCar.state == 0: # If car state is 'charging'
                pass
            elif currentCar.state == 1: # If car state is 'idling'
                pass
            elif currentCar.state == 2: # If car state is 'moving'
                currentCar.moveToward(currentCar.currentNode)    
            elif currentCar.state == 3: # If car state is 'at node'
                pass
        
        #Iterate through all node queues
        for node in self.nodes:
            carClear = []
            currentNode = self.nodes[node]
            for car in self.nodes[node].queue: #Decrease time of each car at node
                currentNode.queue[car] = currentNode.queue[car] - 1
                if self.nodes[node].queue[car] == 0:
                    #Remove from queue
                    carClear.append(car)
            if carClear:
                for car in carClear:
                    self.nodes[node].removeCar(car)
                    car.state = 2
                    car.currentNode = car.task.finish
                    
        print("\n")