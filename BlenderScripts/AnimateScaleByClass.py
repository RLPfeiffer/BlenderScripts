import bpy

# Set the scale values
start_scale = (5, 5, 5)
new_scale = (1, 1, 1)

# Set the frame numbers for the keyframes
start_frame = 575
new_frame = 600

# Iterate over all objects in the scene
for obj in bpy.context.scene.objects:
    # Check if the object's name contains "AJ"
    if "Cav" in obj.name:
        # Set the object's scale at the starting frame
        obj.scale = start_scale
        obj.keyframe_insert(data_path='scale', frame=start_frame)
        
        # Set the object's scale at the new frame
        obj.scale = new_scale
        obj.keyframe_insert(data_path='scale', frame=new_frame)