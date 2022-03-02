import bpy

#Save all of your cell_class colors to the index and access them there to make changing colors easy
cell_class = 'PR(cone)'
alphaChange = bpy.data.collections[cell_class]
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
(1, 0.5, 0, 1), #MC = [9]
(1, 0, 0, 1) #yAC = [10]
]

for ob in alphaChange.objects:
    ob.select_set(True)
    mat = ob.active_material
    #use the corresponding number from your index (number is in the comments)
    mat.diffuse_color = (colorIndex[0])
    mat.keyframe_insert(data_path='diffuse_color', frame = 120)
    mat.diffuse_color = (1, 1, 1, 0)
    mat.keyframe_insert(data_path='diffuse_color', frame = 180)
