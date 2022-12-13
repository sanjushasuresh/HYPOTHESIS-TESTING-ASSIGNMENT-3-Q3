# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:15:02 2022

@author: SANJUSHA
"""

import numpy as np
n1 = 393
n2 = 4064
p = 0.05
p1 = 0.08
p2 = 0.9
a = round(p1*100)
a
b = round(p2*100)
b
props = np.array([a,b])
samplesize = np.array([393,4064])
from statsmodels.stats.proportion import proportions_ztest
stats,p_val = proportions_ztest(props, samplesize)
# H0 = All proportions are equal
# H1 = Not all proportions are equal
if p_val<0.05:
    print("H0 is rejected, H1 is accepted")
else:
    print("H1 is rejected, H0 is accepted")
# Since H1 is rejected and H0 is accepted, we can conclude that all
# proportions are equal i.e. male-female buyer ratios are similar across regions
