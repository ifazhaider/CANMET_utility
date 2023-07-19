import numpy as np
import os
from pylab import load
from scipy import *
from scipy.integrate import simps
from json import *

#home  = '/home/hsimha/CNSC/3d_aecl_g/'
home = path1 = 'C:\\TEMP\\2023_June_K_valid\\ThreeDK\\'
readcont = 2
thickness_index =0
external_face = "min"
Bn = 54

#----contour histories
jcontour_history= open(home+ '/jcontour_hist.txt','r')


fej = load(jcontour_history)
ncnt = len(fej) -1
nthk = len(fej[0])
time = fej[ncnt]
fej = fej[0: ncnt]  #---strip time out 

#----contour fields
jcontour_field= open(home + '/jcontour_field.txt','r')
fejf = load(jcontour_field)

xvalues=[]
for i in range(0,nthk):
   xvalues.append(fejf[readcont][i][1][thickness_index])

Kvalues = fej[readcont]

if external_face=="max":
    Kvalues.reverse()
    xvalues.reverse()

tmp=[]
tmp.append(abs(xvalues[1]- xvalues[0])*(Kvalues[1][0])/2 )

for i in range(2,nthk):
    tmp.append(abs(xvalues[i]- xvalues[i-1])*(Kvalues[i][0]+Kvalues[i-1][0])/2 )   

sum=sum(tmp)
Kavg = sum/(Bn/2 - abs(xvalues[1]- xvalues[0])/2)
print("Kavg =", Kavg)





