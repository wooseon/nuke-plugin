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
import sendToAvconv

# SET KNOB DEFAULTS
# ////////////////////////////////////////////////////////////////////////////////

# WRITE NODE
# use this instead of nuke.addBeforeRender so that artists can remove it locally if needed
nuke.knobDefault('Write.beforeRender', 'pipeline.createWriteDir()')
nuke.knobDefault('Write.afterRender', 'sendToAvconv.sendToAvconv()')

# ROOT
nuke.knobDefault('Root.project_directory', '[python {nuke.script_directory()}]/../')
nuke.addFormat( '2048 1152 0 0 2048 1152 1 2k_16:9' )
nuke.knobDefault('Root.format', '2k_16:9')
nuke.knobDefault('Root.proxy_type', 'scale')
nuke.knobDefault('Root.proxy_scale', '.5')
nuke.knobDefault('Root.fps', '24')

# NODE PRESETS
# ////////////////////////////////////////////////////////////////////////////////
import cam_presets
cam_presets.nodePresetCamera()
import reformat_presets
reformat_presets.nodePresetReformat()

# LUTs
#CB
nuke.knobDefault('Viewer.viewerProcess', 'None')
nuke.knobDefault('monitorLut', 'linear')
nuke.knobDefault('logLut', 'linear')
nuke.knobDefault('int8Lut', 'linear')
nuke.knobDefault('int16Lut', 'linear')

# OTHER
# ////////////////////////////////////////////////////////////////////////////////

#Goofy Titles for untitled scripts
#nuke.untitled = nukescripts.goofy_title()
