import bpy
import bmesh
import os
import numpy as np

#create the folder 

path = '~' 
folder = os.path.exists(path)
n = 20 #the number of the points want to select

if not folder:
    os.makedirs(path) 
    

obj = bpy.context.object

data = obj.data
bm = bmesh.from_edit_mesh(data) #Edit Mode

v = [s.index for s in bm.select_history if isinstance(s, bmesh.types.BMVert)]
file = open(path + '/coodinates.txt','w')

p = np.zeros(shape=(n,3))


for i in range(0,n): 
    
    j = v[i]
    vp = obj.data.vertices[j]
    p[i] = np.array(vp.co)
    
print(p)
np.savetxt(path + '/coodinates.txt', np.matrix(p))