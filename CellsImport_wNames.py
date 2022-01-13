import os
import bpy

#Path to folder containing dae files
cells_path = os.path.join('D:\\', 'Documents\\MeshLabProjects\\RPC1\\Aiis')

file_list = sorted(os.listdir(cells_path))

#get a list of all of the files ending in '.dae'
obj_list = [item for item in file_list if item.endswith('.dae')]
added_obj = bpy.data.collections['Collection']

#loop and add to scence
for item in obj_list:
    objName = os.path.basename(item)
    path_to_file = os.path.join(cells_path, item)
    bpy.ops.wm.collada_import(filepath = path_to_file)
    for ob in added_obj.objects:
        if ob.name == 'node':
            ob.name = ob.name.replace("node", objName)


print('Finished')

