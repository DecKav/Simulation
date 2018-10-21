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
    sim.addNode(0, 0)
    sim.addNode(0, 1)
#    sim.addNode(2, 1)
#    sim.addNode(2, 2)
    sim.addCharger(1, 0)
    sim.addCar(1)
    sim.addCar(2)
    sim.addCar(3)
    sim.addCar(4)
    sim.addCar(5)
    taskNodes1 = OrderedDict() #3 steps = 1
    taskNodes1["00"] = 1
    taskNodes1["01"] = 1
    taskNodes2 = OrderedDict() #6 steps = 2
    taskNodes2["00"] = 2
    taskNodes2["01"] = 3
    #1 hr = 3 steps
    #Start (Step 1, 7 jobs)
    addTasks(sim, 3, 1, taskNodes1)
    addTasks(sim, 2, 1, taskNodes2)
    #Hour 1 (Step 4, 0 jobs)
    addTasks(sim, 0, 4, taskNodes1)
    addTasks(sim, 0, 4, taskNodes2)
    #Hour 2 (Step 7, 4 jobs)
    addTasks(sim, 2, 7, taskNodes1)
    addTasks(sim, 1, 7, taskNodes2)
    #Hour 3 (Step 10, 6 jobs)
    addTasks(sim, 2, 10, taskNodes1)
    addTasks(sim, 2, 10, taskNodes2)
    #Hour 4 (Step 13, 10 jobs)
    addTasks(sim, 1, 13, taskNodes1)
    addTasks(sim, 4, 13, taskNodes2)
    #Hour 5 (Step 16, 6 jobs)
    addTasks(sim, 4, 16, taskNodes1)
    addTasks(sim, 1, 16, taskNodes2)
    #Hour 6 (Step 19, 4 jobs)
    addTasks(sim, 2, 19, taskNodes1)
    addTasks(sim, 1, 19, taskNodes2)
    #Hour 7 (Step 22, 2 jobs)
    addTasks(sim, 0, 22, taskNodes1)
    addTasks(sim, 1, 22, taskNodes2)
    #Hour 8 (Step 25, 0 jobs)
    addTasks(sim, 0, 25, taskNodes1)
    addTasks(sim, 0, 25, taskNodes2)
    #Hour 9 (Step 28, 0 jobs)
    addTasks(sim, 0, 28, taskNodes1)
    addTasks(sim, 0, 28, taskNodes2)
    #Hour 10 (Step 31, 0 jobs)
    addTasks(sim, 0, 31, taskNodes1)
    addTasks(sim, 0, 31, taskNodes2)
    #Hour 11 (Step 34, 0 jobs)
    addTasks(sim, 0, 34, taskNodes1)
    addTasks(sim, 0, 34, taskNodes2)
    #Hour 12 (Step 37, 0 jobs)
    addTasks(sim, 0, 37, taskNodes1)
    addTasks(sim, 0, 37, taskNodes2)
    #End (Step 40)
    
    
    
    print("=======================")
    print("\n")
    return sim

def addTasks(sim, number, time, nodes):
    for i in range(0,number):
        sim.addTask(i, time, nodes)

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
    
