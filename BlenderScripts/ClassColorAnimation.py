import bpy

#Save all of your structure colors to the index and access them there to make changing colors easy
structure = 'PR(cone)'
alphaChange = bpy.data.collections[structure]
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

for ob in alphaChange.objects:
    ob.select_set(True)
    mat = ob.active_material
    #use the corresponding number from your index (number is in the comments)
    mat.diffuse_color = (colorIndex[0])
    mat.keyframe_insert(data_path='diffuse_color', frame = 120)
    mat.diffuse_color = (1, 1, 1, 0)
    mat.keyframe_insert(data_path='diffuse_color', frame = 180)
