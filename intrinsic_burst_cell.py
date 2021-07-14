# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:22:41 2021

@author: Priyanka Patel
"""
import izhikevich_cell as izh
#import numpy as np
#mport matplotlib.pyplot as plt

class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype='Intrinsic Bursting Izhikevich' # Sinusoidal?
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
    
myCell = ibCell(4000)
myCell.simulate()

    
if __name__=='__main__':
    izh.plotMyData(myCell)
    
