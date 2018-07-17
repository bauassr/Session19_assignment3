# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:13:18 2018

@author: avatash.rathore
"""

import numpy as np 
import scipy.stats as stats

X = np.array([10, 20, 30, 40, 50])
Y = np.array([5,10,15, 20, 25])

print("Variance for X : %2.f" %X.var())
print("Variance for Y : %2.f"%Y.var())

print("F- Test = variance of x / Variance of Y \n","F= %2.f" %(X.var()/Y.var()))

print("Degree  of freedom is N-1");
dfX=len(X)-1
dfY=len(Y)-1
print("DF for X :" ,dfX)
print("DF for Y :" ,dfY)

stats.f_oneway(X,Y)
print("The test output yields an F-statistic of 3.6 and a p-value of 0.094.")

