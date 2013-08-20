import os, nuke, nukescripts
import sys

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

# Variable declaration
printf = '.%04d'

# Define function
def customWrite(extension = 'exr', destination = 'server'):
	w = nuke.createNode("Write")
	
	k = nuke.String_Knob("shotdir", "Shot Dir")
	w.addKnob(k)
	k = nuke.String_Knob("filename", "Filename")
	w.addKnob(k)
	
	w.knob("file_type").setValue(extension)
	w.knob("beforeRender").setValue("pipeline.createWriteDir()")
	w.knob("filename").setValue(filename())
	
	# EXR
	if extension == "exr":
		w.knob("shotdir").setValue(shotDir())
		w.knob("file").setValue('[value shotdir]/[value filename]/[value filename]' + printf + '.' + extension)
	# PNG
	elif extension == "png":
		w.knob("shotdir").setValue(shotDir('Review'))
		w.knob("file").setValue('[value shotdir]/[value filename]/[value filename]' + printf + '.' + extension)

def shotDir(folder = 'Comp'):
	return os.path.dirname(os.path.dirname(nuke.root().name())) + '/' + folder
	
def filename():
	return os.path.basename(os.path.splitext(nuke.root().name())[0]) 

# PATHS
# ////////////////////////////////////////////////////////////////////////////////

# CREATE DIR
# Make directory on Save if they don't exist
def createWriteDir():
	file = nuke.filename(nuke.thisNode())
	dir = os.path.dirname( file )
	osdir = nuke.callbacks.filenameFilter( dir )
	try:
		os.makedirs(osdir)
	except OSError:
		pass

# FILENAME FIX
# LionsBay
def filenameFix(filename):
	if nuke.env['WIN32']:
		filename = filename.replace( "/Volumes/The_Forest/", "Z:/" )
	elif nuke.env['MACOS']:
		filename = filename.replace( "Z:/", "/Volumes/The_Forest/" )
	elif nuke.env['LINUX']:
		filename = filename.replace("Z:/", "/media/The_Forest/")
	return filename

nuke.addFilenameFilter(filenameFix)
	
# ADD FAVOURITE DIR
# Arctic Air

#project = 'Arctic_Air_2'
#vol = ''
#if nuke.env['LINUX']:
#	vol = '/media/Projects/'
#	vol2 = '/media/Elements/'
#	vol3 = '/media/Projects/Arctic_Air_2/editorial/from_vfx/'
#elif nuke.env['MACOS']:
#	vol = '/Volumes/Projects/'
#	vol2 = '/Volumes/Elements/'
#	vol3 = '/Volumes/Projects/Arctic_Air_2/editorial/from_vfx/'
#elif nuke.env['WIN32']:
#	vol = 'Z:/'
#	vol2 = 'X:/'
#	vol3 = 'Z:/Projects/Arctic_Air_2/editorial/from_vfx/'

#nuke.addFavoriteDir('Project', vol)
#nuke.addFavoriteDir('Shots', vol + project + '/shots/')
#nuke.addFavoriteDir('Assets', vol + project + '/assets/')
#nuke.addFavoriteDir('Elements', vol2)
#nuke.addFavoriteDir('Editorial', vol3)

