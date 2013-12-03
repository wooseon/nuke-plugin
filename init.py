import nuke

#PLUGIN PATHS
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./lib')
nuke.pluginAddPath('./lut')
nuke.pluginAddPath('./tcl')
nuke.pluginAddPath('./templates')

import os, nukescripts, platform
import pipeline

os.environ['NUKE_PROJECT'] = 'When Calls The Heart'

# SET KNOB DEFAULTS
# ////////////////////////////////////////////////////////////////////////////////

# WRITE NODE
nuke.knobDefault('Write.beforeRender', 'pipeline.createWriteDir()')

# ROOT
nuke.knobDefault('Root.project_directory', '[python {nuke.script_directory()}]/../')
nuke.knobDefault('Root.format', 'HD')
nuke.knobDefault('Root.proxy_type', 'scale')
nuke.knobDefault('Root.proxy_scale', '.5')
nuke.knobDefault('Root.fps', '23.976')

# LUTs
nuke.knobDefault('logLut', 'sRGB')

nuke.ViewerProcess.register("Cineon", nuke.createNode, ("ViewerProcess_1DLUT", "current Cineon"))

#font
nuke.knobDefault("Text.font", "[getenv NUKE_PATH $env(HOME)/.nuke]/fonts/FreeSans.ttf")

# NODE PRESETS
# ////////////////////////////////////////////////////////////////////////////////
import cam_presets
cam_presets.nodePresetCamera()
import reformat_presets
reformat_presets.nodePresetReformat()

