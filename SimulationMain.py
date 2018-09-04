# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

from collections import OrderedDict
from Simulator import Simulator

if __name__ == "__main__":
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(2, 2)
    sim.addCar(1)
    taskNodes = OrderedDict()
    taskNodes["11"] = 2
    taskNodes["22"] = 1
    sim.addTask(1, taskNodes, 5, 1)
        
        
    
    count = 0
    while(count<5):

        sim.timeStep()
        count = count + 1
