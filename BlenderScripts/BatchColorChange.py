import bpy

colorIndex = [
(0.03, 0, 0.6, 1), #PR(cone) = [0]
(0.6, 0.5, 0, 1), #PR(ind) = [1]
(0, 0.5, 0.4, 1), #PR(rod) = [2]
(0, 1, 0, 1), #AiiGAC = [3]
(0, 0.08, 1, 1), #CBa = [4]
(0, 0.8, 0.5, 1), #CBb = [5]
(0.02, 0, 1, 1), #RodBC = [6]
(0.2, 0, 0, 1), #GC = [7]
(0.6, 0.7, 0, 1), #HC = [8]
(0.319, .284, 0.046, 1), #MC = [9]
(1, 0, 0, 1), #yAC = [10]
(0.907, 0, 0.929, 1), #AJ = [11]
(0, 0.929, .308, 1), #Cav = [12]
(1, 0, 0, 1), #GAdj_Inhib = [13]
(0, 1, 0, 1), #GAdj_Ribbon = [14]
(0.104, 0, 1, 1), #NGAJ = [15]
]
#create a material you'll be coloring
mat = bpy.data.materials.new(name='color')
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs['Base Color'].default_value = colorIndex[9]
mat.blend_method = 'BLEND'
mat.use_backface_culling = False
mat.show_transparent_back = False

#iterate over objects in scene
for o in bpy.context.scene.objects:
    if "MC" in o.name:
        #Set the created material as the active material
        o.active_material = mat

