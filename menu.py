import nuke, pipeline, setProjectFrameRange

# TOOLS
# ////////////////////////////////////////////////////////////////////////////////
menubar=nuke.menu("Nodes")
m=menubar.addMenu("Tools")
m.addCommand("Slate", "nuke.createNode('Slate')", index=1, icon="slate.png")
m.addCommand("BurnIn", "nuke.createNode('BurnIn')", index=2, icon="slate.png")
m.addSeparator()

n=m.addMenu("WRITE", icon="Write.png")
n.addCommand("Write DPX", "pipeline.customWrite('dpx')", index=1, icon="Write.png")

n=m.addMenu("LUT", icon=":qrc/images/Toolbar3DLUT.png")

n=m.addMenu("Colour", icon=":qrc/images/ToolbarColor.png")
n.addCommand("Despill Madness", "nuke.createNode('DespillMadness')",  icon="Sphere.png")

n=m.addMenu("Draw", icon=":qrc/images/ToolbarDraw.png")
n.addCommand("FlareFactory Plus", "nuke.createNode('FlareFactory_Plus')", icon="FlareFactoryPlus.png")
n.addCommand("AutoFlare", "nuke.createNode('AutoFlare2')")
n.addCommand("4 Point Gradient", "nuke.createNode('magicCarpet')", icon="magicCarpet.png")

n=m.addMenu("Filter", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("AlphaEdge", "nuke.createNode('AlphaEdge')", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("FieldsKit", "nuke.createNode('FieldsKit')", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("EdgeExtend", "nuke.createNode('EdgeExtend')", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("Chromatic Aberation", "nuke.createNode('akromatism_stRub')", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("Directional Blur", "nuke.createNode('directionalBlur_rk')", icon=":qrc/images/ToolbarFilter.png")
n.addCommand("Bokeh Blur", "nuke.createNode('BokehBlur_4')", icon=":qrc/images/ToolbarFilter.png")

n=m.addMenu("Grain", icon="grain.png")
n.addCommand("REDNoise4", "nuke.createNode('REDNoise4')", index=1, icon="red-noise.png")
n.addCommand("GrainEdge", "nuke.createNode('GrainEdge')", index=2, icon="grain.png")
n.addCommand("GrainControl", "nuke.createNode('GrainControl')", index=3, icon="grain.png")

n=m.addMenu("Transform", icon=":qrc/images/ToolbarTransform.png")
n.addCommand("SmartPin", "nuke.createNode('SmartPin')", icon="ConerPin.png")


# MENUS
# ////////////////////////////////////////////////////////////////////////////////
menubar=nuke.menu("Nuke")

m=menubar.addMenu("&File")
#Version up Comp number
m.addCommand("Save New Comp Version", "pipeline.script_comp_version_up()", index=5 )
m.addCommand("Save New Anim Version", "pipeline.script_anim_version_up()", index=6 )

m=menubar.addMenu("&Edit")
#Set Project Frame Range
m.addCommand("&Node/Set Project Frame Range From Node", setProjectFrameRange.callPanel, '^R')

m = menubar.addMenu("Import and Export")
# Nuke2Maya
import FromNuke2MayaExporter, FromMaya2NukeImporter
m.addCommand("Export Camera as fm2n-File", "FromNuke2MayaExporter.FromNuke2MayaExporter()")
m.addCommand("Import fm2n-File", "FromMaya2NukeImporter.FromMaya2NukeImporter()")
