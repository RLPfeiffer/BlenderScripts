import bpy

# Get the total number of objects with "RPC2" in their names
total_objects = len([obj for obj in bpy.data.objects if "RPC2" in obj.name])

i = total_objects - 1  # Start with the highest index

for object in bpy.data.objects:
    if "RPC2" in object.name:
        object.location = [0.00, 0.000, (30 - (0.4 * i))]
        object.scale = [60.312, 60.312, 1]
        object.keyframe_insert(data_path='location', frame=(3 * i + 1))
        object.location = [-400, 0.00, (30 - (0.4 * i))]
        object.keyframe_insert(data_path='location', frame=(3 * i + 2))
        i = i - 1  # Decrement i in each iteration