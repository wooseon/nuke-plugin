import nuke

#PLUGIN PATHS
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./python')
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
nuke.knobDefault('Root.format', 'HD')
nuke.knobDefault('Root.proxy_type', 'scale')
nuke.knobDefault('Root.proxy_scale', '.5')
nuke.knobDefault('Root.fps', '23.976')

# LUTs
#CB
nuke.ViewerProcess.register("Cineon", nuke.createNode,("ViewerProcess_1DLUT", "current Cineon"))
nuke.knobDefault('Viewer.viewerProcess', 'Cineon')
nuke.knobDefault('monitorLut', 'Cineon')

# OTHER
# ////////////////////////////////////////////////////////////////////////////////

#Goofy Titles for untitled scripts
#nuke.untitled = nukescripts.goofy_title()
