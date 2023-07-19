# contour integrals post processer
# this file is for the history of the J-integral
# pipe line samples
# Python Code for ABAQUS 6.11
# C. Hari Manoj Simha - sept 2015
# modified by B. Williams, August 2018
# modified by I. Haider, 2023
#test 123

from numpy import *
from odbAccess import *
from math import *
import json
import os

#--------------------------------------------------------

nthk = 6  #---number of nodes through thickness
ncnt = 10  #---number of contours
odbname= "5.odb"
path1 = 'C:\\TEMP\\2023_June_K_valid\\ThreeDK\\'

cont_name = []

cont_field_coords = []

#temp_name = 'J at JINT_CRACK1__PICKEDSET19-'
temp_name = 'K1 at H-OUTPUT-1_CRACK-1__PICKEDSET104-'

jcontour_history = open('jcontour_hist.txt', 'w')   #---open file for dumping the stress strain curve
jcontour_field   = open('jcontour_field.txt', 'w')   #---open file for dumping the stress strain curve


for i in range(1,ncnt+1):
    for j in range(1, nthk+1):
     if(i < 10) :
         nam1 = '0'+str(int(i))  #---add prefix 0 in some cases (not sure why)
        # nam1 = str(int(i))
     else:
         nam1 = str(int(i))
     cont_name.append(temp_name+str(j)+'__Contour_'+ nam1)  
 
#---------------------------------------------------------
#   read in the odb file 

#path1 = os.path.join(os.pardir, odbname)
path1 = path1 + odbname
odb = openOdb(path = path1)					#---open the database
#odb = openOdb(path = 'Job-1.odb')				#---open the database

t1 = odb.steps

t2 = t1['Step-1']

t3 = t2.historyRegions

t4 = t3['ElementSet  ALL ELEMENTS']

t5 = t4.historyOutputs



#--------------------------------------------------------
# get contours by group (num of contours ) ncnt
cont_j_group = []

for i in range(ncnt):  
 temp_group = []      #---all j histories in the group
 for j in range(nthk):     
  contname = cont_name[ nthk*i + j]
  t6 = t5[contname]
  t7 = t6.data
  temp_j_node = []  
  temp_time   = []
  
  for k in range(len(t7)):
   temp_j_node.append( t7[k][1])
   temp_time.append( t7[k][0])   
  temp_group.append(temp_j_node)
 cont_j_group.append(temp_group) 
  
#-------------------------------------------------------
# output the contour histories

cont_j_group.append(temp_time)
json.dump(cont_j_group, jcontour_history )


  
jcontour_history.close()

#------------------------------------------------------
# do the field values of the contour for 3d plot 

cont_name = []

temp_name = 'H-OUTPUT-1_CRACK-1_K__PICKEDSET104-'

for i in range(1,ncnt+1):
    for j in range(1, nthk+1):
     if(i < 10) :
         nam1 = '0'+str(int(i))  #---add prefix 0 in some cases (not sure why)
         #nam1 = str(int(i))
     else:
         nam1 = str(int(i))
     print     temp_name+str(j)+'__Contour_'+ nam1
     cont_name.append(temp_name+str(j)+'__Contour_'+ nam1)  
#---------------------------------------------------
# read the odb file 

t1  = odb.rootAssembly             #---get the assembly
t2  = t1.nodeSets                  #----get the node sets
     
#--------------------------------------------------------
# get contours by group (num of contours ) ncnt
for i in range(ncnt):
 temp_group = []        #---araray containing coordinates of contour integral for every thickness
 for j in range(nthk):     
  contname = cont_name[ nthk*i + j]
  t3 = t2[contname]
  t4 = t3.nodes[0]
  temp_coord_array = []  #---array containing indifidual coordiniates
  for k in range(len(t4)):
   x = t4[k].coordinates[0]
   y = t4[k].coordinates[1]
   z = t4[k].coordinates[2] 
   temp_coord_array.append([float(x), float(y), float(z)])
  temp_group.append(temp_coord_array)   
 cont_field_coords.append(temp_group)     
 
json.dump(cont_field_coords, jcontour_field) 
jcontour_field.close()
