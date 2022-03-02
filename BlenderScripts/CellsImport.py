import os
import bpy

#Path to folder containing dae files
cells_path = os.path.join('D:\\', 'Documents\\Blender\\RPC1\\Cell_Dae\\CBas\\')

file_list = sorted(os.listdir(cells_path))

#get a list of all of the files ending in '.dae'
obj_list = [item for item in file_list if item.endswith('.dae')]

#loop and add to scence
for item in obj_list:
    path_to_file = os.path.join(cells_path, item)
    bpy.ops.wm.collada_import(filepath = path_to_file)

print('Finished')
