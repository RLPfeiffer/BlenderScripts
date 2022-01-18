import bpy

#Only the variable cell_class needs to be changed between cell types being categorized, make sure its something unique to all of the cells you want in a single collection
cell_class = 'Aii'
#create a collection folder to move the cell class to
New = bpy.data.collections.new(cell_class)
bpy.context.scene.collection.children.link(New)

#The default collection is typically named 'Collection' if for some reason it has another name change it in the quotes below. 
from_collection = bpy.data.collections['Collection']
to_collection = bpy.data.collections[cell_class]

to_unlink = []
for ob in from_collection.objects:
    if cell_class in ob.name:
        try:
            to_collection.objects.link(ob)
        except RuntimeError:
            pass
        to_unlink.append(ob)
    
for ob in to_unlink:
    from_collection.objects.unlink(ob)
