import os
import bpy


# make sure the car obj is in the same directory as your script
blender_file = os.getcwd() + "/BMW_X5_4.obj"

bpy.ops.import_scene.obj(filepath=blender_file)

# loop through all the objects in the scene
scene = bpy.context.scene
#print(bpy.context.selected_objects)
# deselect all objects
for ob in bpy.data.objects:
    ob.select = False

for select_obj in bpy.data.objects:
    select_obj.select = True
    bpy.ops.export_scene.obj(filepath = os.getcwd() + select_obj.name + ".obj", use_selection = True)
    select_obj.select = False
print(bpy.context.selected_objects)