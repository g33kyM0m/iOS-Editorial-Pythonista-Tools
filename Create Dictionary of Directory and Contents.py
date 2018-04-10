# Creates & Saves a .json Dictionary File with the Current Directory's Contents 
# (files and sub-directories, as well as files within those sub-directories)
# Designed to work with Pythonista (iOS app) & most other Python environments

# Original Inspiration from Stack Overflow
# link: https://stackoverflow.com/a/25226267

# This Version designed by g33kym0m (www.g33kymom.com) 


import console, json, os

# SET INITIAL VARIABLES
myPath = os.getcwd()
myPathGet = myPath.split('/')
myPathCount = (len(myPathGet))-1
myPathName = myPathGet[myPathCount]
fileName = 'Contents - ' + myPathName + '.json'
divdr = '=========='*4
nl = '\n'


# DEFINE METHOD TO CREATE DICTIONARY FROM DIRECTORY
def path_to_dict(path):
	fn = os.path.basename(path)
	d = {'name': fn}
	if os.path.isdir(path):
		d['type'] = "directory"
		d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
	else:
		d['type'] = "file"
		ex = fn.split('.')
		d['ext'] = ex[-1]
	return d


# CREATE DICTIONARY AND MODIFY WITH FORMATTED NAME OF CURRENT DIRECTORY
dirDict = path_to_dict(myPath)
dirDict['name'] = myPathName
newData = json.dumps(dirDict)


# CREATE DICTIONARY LOCAL FILE, SAVE, & CLOSE
newDict = open(fileName, 'w')
newDict.write(newData)
newDict.close()


# CONSOLE OUTPUT FOR VISUAL CONFIRMATION
console.clear()
print divdr + nl + nl
print 'Directory Dictionary for: ' + myPathName
print nl + nl + divdr + nl + nl
print 'New Dictionary Preview:' + nl + nl
print newData
print nl + nl + divdr
print nl + nl + 'New Dictionary Saved to: ' + fileName
print nl + nl + divdr

