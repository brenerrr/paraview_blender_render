from paraview.simple import *

output_path = f"path/to/x3d/folder/"

paraview.simple._DisableFirstRenderCameraReset()
scene = GetAnimationScene()

tstart = int(scene.StartTime)
tend = int(scene.EndTime)

for i in range(tend+1):
    scene.AnimationTime = i
    renderView1 = GetActiveViewOrCreate('RenderView')
    source = GetActiveSource()
    display = GetDisplayProperties(source, view=renderView1)
    ExportView(f'{output_path}/{i:06d}.x3d', view=renderView1)




