# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:03:50 2015

@author: ahmetkaya

"""
import random
import matplotlib.pyplot as plt

def neg_exp(lambd):
    return random.expovariate(lambd)
 
 
class Customers(object):
    
    def __init__(self,arrivalTime,serviceTime,serviceStartTime):
        self.arrivalTime = arrivalTime
        self.serviceStartTime = serviceStartTime
        self.serviceTime = serviceTime
        self.wait=self.serviceStartTime - self.arrivalTime
        self.serviceEndTime=self.arrivalTime + self.serviceTime


def runSimulation(lamda=False,mu=False, totalSimTime=False):
    if not lamda:
        print "Need to enter arrival rate lamda:"
    if not mu:
        print "Need to enter service rate mu:"
    if not totalSimTime:
        print "Need to enter totalSimTime:"
    
    customers=[]
    
    t=0
    
    while t< totalSimTime:
        
        if len(customers)==0:
            arrivalt=neg_exp(lamda)
            serviceSt=arrivalt
        else:
            arrivalt=arrivalt+neg_exp(lamda)
            serviceSt=max(arrivalt,customers[-1].serviceEndTime)
        servicet=neg_exp(mu)
        print servicet
        
        customers.append(Customers(arrivalt,servicet,serviceSt))
        t= arrivalt
    
    Waits=[a.wait for a in customers]
    Mean_Wait=sum(Waits)/len(Waits)

    Total_Times=[a.wait+a.serviceTime for a in customers]
    Mean_Time=sum(Total_Times)/len(Total_Times)

    Service_Times=[a.serviceTime for a in customers]
    Mean_Service_Time=sum(Service_Times)/len(Service_Times)

    Utilisation=sum(Service_Times)/sum(Total_Times)
    
    print ""
    print "Summary results:"
    print ""
    print "Number of customers: ",len(customers)
    print "Mean Service Time: ",Mean_Service_Time
    print "Mean Wait: ",Mean_Wait
    print "Mean Time in System: ",Mean_Time
    print "Utilisation: ",Utilisation
    print ""
    plt.hist(Waits)
    plt.title("total time:%f utilization:%f"%(sum(Total_Times),Utilisation))
