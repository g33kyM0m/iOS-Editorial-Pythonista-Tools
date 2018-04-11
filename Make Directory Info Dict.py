# Create a json dictionary file in current directory with its name, path, and 'parent' directories. 
# Useful to streamline current and future Editorial & Pythonista projects.

# by g33kym0m - www.g33kymom.com
# from https://github.com/g33kyM0m/iOS-Editorial-Pythonista-Tools

import os, json, editor

i = 1
neg = -2
jn = '/'

# GET CURRENT DIRECTORY NAME AND PATH USING CURRENT DOC
pth = editor.get_path()
dirList = pth.split(jn)
here = jn.join(dirList[0:-1])
dirList = here.split(jn)
dirName = dirList[-1]

# GET LOCATION OF MAIN (DOCUMENTS) DIRECTORY IN TREE
dirFind = 'Documents'
findLoc = dirList.index(dirFind)
allCnt = len(dirList)
parCnt = allCnt - findLoc

# CREATE PARENT DIRECTORY LIST
parents = {}

while i < parCnt:
	p = dirList[neg]
	parents[i] = p
	i = i+1
	neg = neg+(-1)


final = {'name': dirName, 'location': here, 'parents': parents}

finalDict = json.dumps(final)

# CREATE & SAVE DATA DICTIONARY FILE
dName = 'dir_info.json'
dFile = open(dName, 'w')
dFile.write(finalDict)
dFile.close()
