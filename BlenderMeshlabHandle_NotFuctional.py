import bpy
import pymeshlab
import numpy      



def exportToMeshLab(blenderMesh):
    # NB pymeshlab is fussy
    # verts and faces have to be provided in a numpy array with verts as type float64 and faces as int32
    # faces have to be triangulated - quads and ngons are not allowed
    
    verts = []  #numpyp.empty((0,3), float64)
    for v in blenderMesh.vertices:
            verts.append([v.co[0], v.co[1], v.co[2]])
    verts = numpy.asarray(verts, dtype=numpy.float64)
    if len(verts) == 0:
        print("No vertices were found, so function aborting")
        return
#    print(verts.shape)   # must report (numOfVerts, 3)
#    print(verts.dtype.name)   # must report float64


    faces = []
    tooManyVerts = False
    for poly in blenderMesh.polygons:
        curFace = []
        for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
            curFace.append(blenderMesh.loops[loop_index].vertex_index)
        if len(curFace) == 3:
            faces.append(curFace)
        else:
            tooManyVerts = True
            
            
    if tooManyVerts:
        print("WARNING: Meshlab will only accept faces with THREE vertices")
    if len(faces) == 0:
        print("No triangular faces were found, so function aborting")
        return
    faces = numpy.asarray(faces, dtype=numpy.int32)
#    print(faces.shape)   # must report (numOfVerts, 3)
#    print(faces.dtype.name)

    # create a new Mesh with the two arrays
    meshlabMesh = pymeshlab.Mesh(verts, faces)

    # create a new MeshSet (a meshset can have multiple meshes each in a differnt layer - but that's not covered with this function)
    meshlabMeshSet = pymeshlab.MeshSet()

    # add the mesh to the MeshSet with the current name
    meshlabMeshSet.add_mesh(meshlabMesh, blenderMesh.name)

    return meshlabMeshSet


def importMeshFromMeshLab(meshlabMesh):
    # NB from_pydata in Blender is fussy
    # verts and faces have to be provided in a standard Python list (NOT a numpy array)
    
    verts = meshlabMesh.current_mesh().vertex_matrix().tolist()
    faces = meshlabMesh.current_mesh().face_matrix().tolist()
    #name = meshlabMesh.current_mesh().mesh_name()   # TODO: return this
    
    return verts, faces  #, name


print("START")

# Export a Blender mesh to MeshLab
me = bpy.context.object.data
meshlabMeshSet = exportMeshToMeshLab(me)

# Import a MeshLab mesh to Blender
verts, faces = importMeshFromMeshLab(meshlabMeshSet)
mesh = bpy.data.meshes.new("meshFromMeshLab")  # add the new mesh
mesh.from_pydata(verts, [], faces)   # this could also be done as a bmesh too...
ob = bpy.data.objects.new("meshFromMeshLab", mesh)
bpy.context.collection.objects.link(ob)


print(verts)
print(faces)

print("DONE")
