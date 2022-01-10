
import bpy

for o in bpy.context.scene.objects:
    o.name = o.name.replace("node-Struct-", "CBa")
