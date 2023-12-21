import bpy

cell_class = 'PR(ind)'
move_coll = bpy.data.collections[cell_class]

for ob in move_coll.objects:
    ob.select_set(True)
    ob.location.z = 120
    
