import bpy

cell_class = 'PR'
move_coll = bpy.data.collections[cell_class]

for ob in move_coll.objects:
    ob.select_set(True)
    ob.keyframe_insert(data_path='location', frame = 0)
    ob.location.z += 120
    ob.keyframe_insert(data_path='location', frame = 60)
