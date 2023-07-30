import os
import bpy

# Inputs
x3d_path = r"C:\Users\brene\Downloads\paraview\data"
output_path = r"C:\Users\brene\Downloads\paraview\output"
surface_file = r"C:\Users\brene\Downloads\paraview\wing_filled.x3d"
use_paraview_camera = True


if not os.path.isdir(output_path):
    os.makedirs(output_path)

# List x3d files
files = os.listdir(x3d_path)
x3d_files = [file for file in files if file.endswith("x3d")]
x3d_files.sort(key=lambda x: '{0:0>8}'.format(x).lower())

# Delete everything in the current scene except for the camera
for object in bpy.data.objects:
    if object.name != "Camera":
        bpy.data.objects.remove(object)

# Try loading a surface file
try:
    bpy.ops.import_scene.x3d(filepath=surface_file)
    surface_mesh = [object for object in bpy.data.objects if object.type == "MESH"][0]
    bpy.context.view_layer.objects.active = surface_mesh
    surface_mesh.material_slots[0].material = bpy.data.materials.get("Surface Material")
    print("Surface loaded")

except:
    print("Could not load surface")

material = bpy.data.materials.get("Material")
scene = bpy.context.scene

# Move current objects to permanent collection
for object in bpy.data.objects:
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.move_to_collection(collection_index=2)

collection = bpy.data.collections["Collection"]

for file in x3d_files:

    print(f"Loading file {file}")

    # Clean scene up
    for object in collection.objects:
        bpy.data.objects.remove(object)

    # Load data
    bpy.ops.import_scene.x3d(filepath=f"{x3d_path}/{file}")

    # Get rid of default lights
    lights = [object for object in collection.objects if "light" in object.name.lower()]
    for light in lights:
        bpy.data.objects.remove(light)

    # Assign material to mesh
    mesh = [object for object in collection.objects if object.type == "MESH"][0]
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.shade_smooth()
    mesh.material_slots[0].material = material

    # Set paraview camera
    if use_paraview_camera:
        camera = collection.objects['Viewpoint']
        bpy.context.scene.camera = camera

    # Render
    filename = file.replace("x3d", "png")
    bpy.ops.render.render()

    # Save render image
    filepath=f"{output_path}/{filename}"
    bpy.data.images['Render Result'].save_render(filepath=filepath)


print("DONE")

