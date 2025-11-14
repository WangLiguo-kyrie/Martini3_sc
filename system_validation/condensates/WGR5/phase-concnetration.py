#! /usr/bin/python

import sys
import os
import numpy as np

import pandas as pd


intervals=[2000,4000,6000,8000,10000]
factor=1347/1530
data=[]
with open('phase.txt','w') as g:
    print('Begin\tEnd\tDiluteconcentration\tDenseconcentration',file=g)
    for i in range(4):
        former=intervals[i]
        latter=intervals[i+1]
        print('density interval: {} to {}'.format(former,latter))

        filename='density-{}_{}ns.xvg'.format(former,latter)
        print(filename)
        os.system("sed -i 's/^@/#/g' %s " %filename)
        data_interval = np.loadtxt(filename)
        print(data_interval.shape)
        #Dilute phase
        dilute1=data_interval[(data_interval[:,0]>12)]
        dilute2=data_interval[(data_interval[:,0]<-12)]
        dilute_conc=(np.mean(dilute1[:,1])+np.mean(dilute2[:,1]))*factor/2
        #Dense phase
        dense=data_interval[((data_interval[:,0]>-5)&(data_interval[:,0]<5))]*factor
        print(dense)
        dense_conc=(np.mean(dense[:,1]))
        print('{}\t{}\t{}\t{}'.format(former,latter,dilute_conc,dense_conc),file=g)



