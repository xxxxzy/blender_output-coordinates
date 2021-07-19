import bpy
import bmesh
import os
import numpy as np
import bpy_extras
from mathutils import Matrix
from mathutils import Vector

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


p = np.zeros(shape=(n,3))
pixel = np.zeros(shape=(n,2))


def project_by_object_utils(cam, point):
    scene = bpy.context.scene
    co_2d = bpy_extras.object_utils.world_to_camera_view(scene, cam, point)
    render_scale = scene.render.resolution_percentage / 100
    render_size = (
            int(scene.render.resolution_x * render_scale),
            int(scene.render.resolution_y * render_scale),
            )
    return Vector((co_2d.x * render_size[0], render_size[1] - co_2d.y * render_size[1]))

cam = bpy.data.objects['Camera1']

for i in range(0,n): 
    
    obMat = obj.matrix_world
    j = v[i]
    vp = obj.data.vertices[j]
    q = obMat @ vp.co
    p[i] = q
    pixel[i] = project_by_object_utils(cam,q)
    
#print(pixel)
 
file = open(path + '/coodinates_3d.txt','w')
file = open(path + '/coodinates_2d.txt','w')
    
np.savetxt(path + '/coodinates_3d.txt', p)
np.savetxt(path + '/coodinates_2d.txt', pixel)




