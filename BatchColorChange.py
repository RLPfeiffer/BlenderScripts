import bpy

#create a material you'll be coloring
mat = bpy.data.materials.new(name= 'colored')

#iterate over objects in scene
for o in bpy.context.scene.objects:
    if "CBa" in o.name:
        #Set the created material as the active material
        o.active_material = mat
        #Set colors using R,G,B,opacity formatting
        mat.diffuse_color = (.004, .130, 1, 1)


