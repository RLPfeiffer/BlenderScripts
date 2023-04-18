import bpy

# Set the structure name and starting alpha value
structure_name = "Cav"
starting_alpha = 0

# Iterate over all objects in the scene
for obj in bpy.context.scene.objects:
    # Check if the object's name contains the structure name
    if structure_name in obj.name:
        # Get the material of the object
        mat = obj.active_material
        # Set the starting alpha value (Alpha is node.inputs 21)
        mat.node_tree.nodes["Principled BSDF"].inputs[21].default_value = starting_alpha
        # Insert keyframe for the starting alpha value
        mat.node_tree.nodes["Principled BSDF"].inputs[21].keyframe_insert("default_value", frame=420)
        # Set the new alpha value
        new_alpha = 1
        mat.node_tree.nodes["Principled BSDF"].inputs[21].default_value = new_alpha
        # Insert keyframe for the new alpha value
        mat.node_tree.nodes["Principled BSDF"].inputs[21].keyframe_insert("default_value", frame=450)

