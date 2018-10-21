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

def setup():
    print("=======================")
    sim = Simulator()
    sim.addNode(1, 1)
    sim.addNode(1, 2)
    sim.addNode(2, 1)
    sim.addNode(2, 2)
    sim.addCharger(1, 3)
    sim.addCar(1)
    sim.addCar(2)
    taskNodes1 = OrderedDict()
    taskNodes1["11"] = 1
    taskNodes1["12"] = 1
    taskNodes1["11"] = 1
    sim.addTask(1, taskNodes1)
    sim.addTask(3, taskNodes1)
    sim.addTask(5, taskNodes1)
    sim.addTask(7, taskNodes1)
    taskNodes2 = OrderedDict()
    taskNodes2["21"] = 1
    taskNodes2["22"] = 1
    taskNodes2["21"] = 1
    sim.addTask(2, taskNodes2)
    sim.addTask(4, taskNodes2)
    sim.addTask(6, taskNodes2)
    sim.addTask(8, taskNodes2)
    
    
    print("=======================")
    print("\n")
    return sim

def optimise():
    """
    Set initial guess (worst case with finite sol) thresholds for:
        Send to charge if task available vs take task (Thresh1)
        Send to charge if no task available vs send to idle (Thresh2)
    While timestep == true
        Simulate operation, count steps
    Second guess thresholds
    While timestep == true
        Simulate operation, count steps
    Based on time steps from guesses, new guess to converge on optimal solution
    Return thresholds, time steps, and optimal solution
    """
    simulator = setup()
    thresh1 = 40
    thresh2 = 100
    
    finish = False
    
    while(finish == False):
        finish = simulator.timeStep(thresh1, thresh2)
        
    first = simulator.time
    
    return first
    
def lookAhead(window):
    """
    For next x time steps, calculate:
        Job Cost = Pending cost + New Cost this step - Cost completed(#cars (u1))
        Charge = Total Charge + Car Charge Gained - Car Charge lost Working(#cars (u2))
    
    Transition cost of distance*move cost
    
    Optimise wrt u1, u2 given New cost this step disturbance
    
    
    """
    simulator = setup()
    cost = []
    charge = []
    for i in range(0,window):
        simulator.timeStep(40, 100)
        cost.append(simulator.totalCost)
        charge.append(simulator.totalEnergy)
        
    return cost, charge
    
    

if __name__ == "__main__":
    print(optimise())
    
    print(lookAhead(2))
