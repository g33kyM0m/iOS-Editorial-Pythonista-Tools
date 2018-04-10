# Create a text list and json dictionary of Error Codes & Explanations. Also displays the data in the console. Useful when troubleshooting tricky scripts. Depending on need, can comment out 1 or more output options.

# by g33kym0m - www.g33kymom.com
# from https://github.com/g33kyM0m/iOS-Editorial-Pythonista-Tools

import os, console, json, re

nl = '\n'
dvr = '=========='*4
dvrLn = nl + dvr + nl
i = 1
x = 0
codeDict = {}
codeList = []
noList= []

# Get & parse Error Codes & Descriptions
for i in range(1,107):
	curCode = os.strerror(i)
	testStr = re.compile(r'[Unknown|Undefined]')	
	strA = 'Unknown'
	strB = 'Undefined'
	if i < 10: curID = 'Error 00' + str(i)
	if i < 100 and i > 9: curID = 'Error 0' + str(i)
	if i > 99: curID = 'Error ' + str(i)
	curTxt = curID + ': ' + curCode
	curTest = testStr.search(curTxt)
	
	if strA not in curTxt and strB not in curTxt:
		codeList.append(curTxt)
		codeDict[i] = {'ID': curID, 'Explanation': curCode}
		i = i + 1
	
	if strA in curTxt or strB in curTxt:
		noList.append(curTxt)
		x = x + 1
		i = i + 1

# Get data ready for output
finalList = nl.join(codeList)
finalNoList = nl.join(noList)
finalDict = json.dumps(codeDict)

##################
# OUTPUT OPTIONS #
##################

# Create List of Error Codes
liFN = 'Error Code List.txt'
liFile = open(liFN, 'w')
liFile.write(finalList)
liFile.close()

# Create json Dictionary of Error Codes
dtFN = 'Error Code Dictionary.json'
dtFile = open(dtFN, 'w')
dtFile.write(finalDict)
dtFile.close()

# Format & Display Error Code Info in Console
console.clear()
print nl + dvrLn + nl
print '+++++ CODE LIST +++++'
print nl + dvrLn + nl
print finalList
print nl + dvrLn + nl
print '+++++ CODE DICTIONARY +++++'
print nl + dvrLn + nl
print finalDict
print nl + dvrLn + nl
print '+++++ NO CODE LIST +++++'
print nl + nl
print 'Unknown Errors Counted = ' + str(x)
print nl
print finalNoList
print nl + dvrLn + nl
