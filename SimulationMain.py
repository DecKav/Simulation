# -*- coding: utf-8 -*-
"""
A simulation for an intelligent warehouse, using cars, nodes, and a parent simulator.


@author: Declan Kavanagh
@author: Sam Bloom

"""

from collections import OrderedDict
from Simulator import Simulator

if __name__ == "__main__":
    
    print("Initialisation:")
    print("")
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(2, 2)
    sim.addNode(1, 2)
    sim.addCar(1)
    taskNodes = OrderedDict()
    taskNodes["11"] = 2
    taskNodes["22"] = 3
    taskNodes["12"] = 2
    sim.addTask(1, taskNodes, 1)
    print("\n")
    
    count = 0
    while(count<15):

        sim.timeStep()
        count = count + 1
