
import bpy

#use this to rename the auto generated node-Structure with wanted identifier
for o in bpy.context.scene.objects:
    o.name = o.name.replace("node-Struct-", "CBa")
