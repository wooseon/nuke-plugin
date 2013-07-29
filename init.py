import nuke

#PLUGIN PATHS
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./tcl')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./lib')
nuke.pluginAddPath('./lut')

import os, nukescripts, platform
import pipeline

# SET KNOB DEFAULTS
# ////////////////////////////////////////////////////////////////////////////////

# WRITE NODE
# use this instead of nuke.addBeforeRender so that artists can remove it locally if needed
nuke.knobDefault('Write.beforeRender', 'pipeline.createWriteDir()')

# ROOT
nuke.knobDefault('Root.project_directory', '[python {nuke.script_directory()}]/../')
nuke.knobDefault('Root.format', 'HD')
nuke.knobDefault('Root.proxy_type', 'scale')
nuke.knobDefault('Root.proxy_scale', '.5')
nuke.knobDefault('Root.fps', '23.976')

# NODE PRESETS
# ////////////////////////////////////////////////////////////////////////////////
import cam_presets
cam_presets.nodePresetCamera()
import reformat_presets
reformat_presets.nodePresetReformat()

# LUTs
#Example
#nuke.knobDefault('Viewer.viewerProcess', 'rec709')
#nuke.knobDefault('monitorLut', 'rec709')
#nuke.knobDefault('floatLut', 'rec709')
nuke.ViewerProcess.register("FOR v1 REC709", nuke.Node, ("ViewerProcess-DFC_v01_REC709.gizmo", ""))
#nuke.ViewerProcess.register("Blur", nuke.createNode, ("Blur", "size 10"))

# OTHER
# ////////////////////////////////////////////////////////////////////////////////
