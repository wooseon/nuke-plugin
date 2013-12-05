import os, nuke, nukescripts
import sys, re

# COMP UP
# Versions up c01 and a01 in filenames
# ////////////////////////////////////////////////////////////////////////////////

def script_comp_version_up():
	"""Adds 1 to the _c## at the end of the script name and saves a new version."""
	root_name = nuke.toNode("root").name()
	(prefix, v) = nukescripts.version_get(root_name, "c")
	if v is None: return

	v = int(v)
	nuke.scriptSaveAs(nukescripts.version_set(root_name, prefix, v, v + 1))

	def script_anim_version_up():
		"""Adds 1 to the _a## at the end of the script name and saves a new version."""
		root_name = nuke.toNode("root").name()
		(prefix, v) = nukescripts.version_get(root_name, "a")
		if v is None: return

		v = int(v)
		nuke.scriptSaveAs(nukescripts.version_set(root_name, prefix, v, v + 1))

# WRITE NODES
# ////////////////////////////////////////////////////////////////////////////////

# Define function
def customWrite(folder = 'Comp', extension = 'exr'):

	#variables
	printf = '.%04d'
	project = '[value project_directory]'
	shot = '[file tail [file dirname [file dirname [value root.name]]]]'
	filename = '[file rootname [file tail [value root.name]]]'

	if extension == "mov":
		if folder == 'Review':
			a = nuke.nodes.Overlays(
				RulersToggle_ctrl = 0,
				LetterboxToggle_ctrl = 0
				)
			a.setInput(0, nuke.selectedNode())
			a.setSelected(True)
		t = nuke.nodes.AddTimeCode( 
			useFrame = 1, 
			frame = 0,
			startcode = '01:00:00:00' 
			)
		t.setInput(0, nuke.selectedNode())
		t.setSelected(True)

	w = nuke.nodes.Write()

	w.setInput(0, nuke.selectedNode())

	w["file_type"].setValue(extension)
	w["beforeRender"].setValue("pipeline.createWriteDir()")
	w["label"].setValue(folder.upper())
	w["file"].setValue(project + folder + '/'+ filename + '/'+ filename + printf + '.' + extension)

	if extension == "mov":
		w["colorspace"].setValue('sRGB')
		w["writeTimeCode"].setValue('1')
		w["file"].setValue(project + folder + '/'+ filename + '.' + extension)
		if folder == 'Review':
			w["codec"].setValue('apcn')
			w["settings"].setValue('000000000000000000000000000001cc7365616e000000010000000100000000000001b876696465000000010000000f00000000000000227370746c0000000100000000000000006170636e000000000018000003ff000000207470726c000000010000000000000000000000000017f9db00000000000000246472617400000001000000000000000000000000000000530000010000000100000000156d70736f00000001000000000000000000000000186d66726100000001000000000000000000000000000000187073667200000001000000000000000000000000000000156266726100000001000000000000000000000000166d70657300000001000000000000000000000000002868617264000000010000000000000000000000000000000000000000000000000000000000000016656e647300000001000000000000000000000000001663666c67000000010000000000000000004400000018636d66720000000100000000000000006170706c00000014636c75740000000100000000000000000000003263646563000000010000000000000000696370746e636c630002000200020100000000010000000100010001ff010000001c766572730000000100000000000000000003001c00010000')
		elif folder == 'Comp':
			w["codec"].setValue('ap4h')
			w["settings"].setValue('000000000000000000000000000001cc7365616e000000010000000100000000000001b876696465000000010000000f00000000000000227370746c00000001000000000000000061703468000000000018000003ff000000207470726c000000010000000000000000000000000017f9db00000000000000246472617400000001000000000000000000000000000000530000010000000100000000156d70736f00000001000000000000000000000000186d66726100000001000000000000000000000000000000187073667200000001000000000000000000000000000000156266726100000001000000000000000000000000166d70657300000001000000000000000000000000002868617264000000010000000000000000000000000000000000000000000000000000000000000016656e647300000001000000000000000000000000001663666c67000000010000000000000000004400000018636d66720000000100000000000000006170706c00000014636c75740000000100000000000000000000003263646563000000010000000000000000696370746e636c63000200020002010000000001000000010001000000020000001c766572730000000100000000000000000003001c00010000')
	elif extension == "exr":
		w["metadata"].setValue(2)


# PATHS
# ////////////////////////////////////////////////////////////////////////////////

# CREATE DIR
# Make directory on Save if it doesn't exist
def createWriteDir():
	file = nuke.filename(nuke.thisNode())
	dir = os.path.dirname( file )
	osdir = nuke.callbacks.filenameFilter( dir )
	try:
		os.makedirs(osdir)
	except OSError:
		pass

# FILENAME FIX
def filenameFix(filename):
	if nuke.env['WIN32']:
		filename = filename.replace( "/Volumes/Projects/", "Z:/" ).replace("/media/Projects/", "Z:/").replace( "/Volumes/Elements/", "Y:/" ).replace("/media/Elements/", "Y:/").replace( "/Volumes/Review/", "X:/" ).replace("/media/Review/", "X:/")
	elif nuke.env['MACOS']:
		filename = filename.replace( "Z:/", "/Volumes/Projects/" ).replace( "/media/Projects/", "/Volumes/Projects/" ).replace( "X:/", "/Volumes/Review/" ).replace( "/media/Review/", "/Volumes/Review/" ).replace( "Y:/", "/Volumes/Elements/" ).replace( "/media/Elements/", "/Volumes/Elements/" )
	elif nuke.env['LINUX']:
		filename = filename.replace("Z:/", "/media/Projects/").replace("/Volumes/Projects/", "/media/Projects/").replace("X:/", "/media/Review/").replace("/Volumes/Review/", "/media/Review/").replace("Y:/", "/media/Elements/").replace("/Volumes/Elements/", "/media/Elements/")
		return filename

		nuke.addFilenameFilter(filenameFix)

# # ADD FAVOURITE DIR
# project = 'Arctic_Air_3'
# vol = ''
# if nuke.env['LINUX']:
# 	vol = '/media/Projects/'
# 	vol2 = '/media/Elements/'
# 	vol3 = '/media/Projects/Arctic_Air_3/editorial/from_vfx/'
# elif nuke.env['MACOS']:
# 	vol = '/Volumes/Projects/'
# 	vol2 = '/Volumes/Elements/'
# 	vol3 = '/Volumes/Projects/Arctic_Air_3/editorial/from_vfx/'
# elif nuke.env['WIN32']:
# 	vol = 'Z:/'
# 	vol2 = 'Y:/'
# 	vol3 = 'Z:/Projects/Arctic_Air_3/editorial/from_vfx/'

# nuke.addFavoriteDir('Project', vol)
# nuke.addFavoriteDir('Shots', vol + project + '/shots/')
# nuke.addFavoriteDir('Assets', vol + project + '/assets/')
# nuke.addFavoriteDir('Elements', vol2)
# nuke.addFavoriteDir('Editorial', vol3)

