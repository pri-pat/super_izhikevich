# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:23:15 2021

@author: Priyanka Patel
"""

import izhikevich_cell as izh


class cCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype='Intrinsic Bursting Izhikevich' # Sinusoidal?
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        self.stimVal = stimVal
    
myCell = cCell(4000)
myCell.simulate()

    
if __name__=='__main__':
    izh.plotMyData(myCell)
    
