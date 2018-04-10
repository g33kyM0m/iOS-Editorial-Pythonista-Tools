# Create a json dictionary file in current directory with its name, path, and 'parent' directories. Useful to streamline current and future Editorial & Pythonista projects.

# by g33kym0m - www.g33kymom.com
# from https://github.com/g33kyM0m/iOS-Editorial-Pythonista-Tools

import os, json

i = 1
neg = -2

here = os.path.abspath(os.curdir)
dirList = here.split('/')
dirName = dirList[-1]

dirFind = 'Documents'
findLoc = dirList.index(dirFind)
allCnt = len(dirList)
parCnt = allCnt - findLoc

parents = {}

while i < parCnt:
	p = dirList[neg]
	parents[i] = p
	i = i+1
	neg = neg+(-1)


final = {'name': dirName, 'location': here, 'parents': parents}

finalDict = json.dumps(final)



dName = 'dir_info.json'
dFile = open(dName, 'w')
dFile.write(finalDict)
dFile.close()
