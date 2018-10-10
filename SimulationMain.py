# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

"""
Energy cost of jobs
"""


from collections import OrderedDict
from Simulator import Simulator

if __name__ == "__main__":
    print("=======================")
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(2, 1)
    sim.addNode(1, 2)
    sim.addCharger(2, 2)
    sim.addCar(1)
    sim.addCar(2)
    taskNodes1 = OrderedDict()
    taskNodes1["11"] = 2
    taskNodes1["21"] = 3
    taskNodes1["12"] = 2
    sim.addTask(1, taskNodes1)
    taskNodes2 = OrderedDict()
    taskNodes2["21"] = 1
    taskNodes2["12"] = 1
    taskNodes2["11"] = 1
    sim.addTask(5, taskNodes2)
    
#    sim = Simulator()
#    
#    sim.addNode(1,1)
#    sim.addNode(3,1)
#    sim.addCharger(2,2)
#    
#    sim.addCar(1)
#    sim.addCar(2)
#    
#    taskNodes1 = OrderedDict()
#    taskNodes1["31"] = 4
#    taskNodes1["11"] = 2
#    taskNodes1["31"] = 3
#    
#    sim.addTask(taskNodes1)
    
    print("=======================")
    print("\n")
    
    count = 0
    while(count<10):

        sim.timeStep()
        count = count + 1
