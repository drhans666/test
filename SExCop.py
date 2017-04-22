#! python3

#roboCopy.py -Copy files with defined extension from specified directory to another spec. dir.
#Currently works only on Linux/MacOS

import re, os, shutil

# gets and checks directory, You want to copy files from
def inFolder():
    while True:
        print('Enter input directory:')
        inputFolder = str(input())
        if os.path.exists(inputFolder) == True:
            break
        else:
            print('Folder does not exists')
    return inputFolder

# gets/checks/eventually creates directory, You want copy files to
def outFolder():
    while True:
        print('Enter output directory:')
        outputFolder = str(input())
        if os.path.exists(outputFolder) == True:
            break
        else:
            os.makedirs(outputFolder)
            break
    return outputFolder

# regex filter that finds files in input
def filter():
    filterRegex = re.compile('([-a-zA-Z0-9+_ |/\'`:~]+)([.])(%s)' %extension)
    return filterRegex

# searching engine that walks through the folders with regex filter; returns matches
def searchForMatches(inputFolder, filterRegex):
    matches = []
    for folderName, subfolders, filenames in os.walk(inputFolder):
        print('Processing Folders: ' + folderName)
        for subfolder in subfolders:
             print('Processing Subfolders:' + folderName + '/' + subfolder)
        for fileName in filenames:
            print('Processing Files:' + folderName + '/' + fileName)
            for groups in filterRegex.findall(folderName + '/' + fileName):
                matches.append(groups[0] + '.' + extension)
    return matches

# copy module
def copyMatches(matches, outputFolder):
    for match in matches:
        shutil.copy(str(match), str(outputFolder))

# main part
print('SExCop 7000 - Selective Extension Copy by drHans\nChoose Your files extension:')
extension = str(input())
inputFolder = inFolder()
outputFolder = outFolder()
filterRegex = filter()
matches = searchForMatches(inputFolder, filterRegex)
filter()
searchForMatches(inputFolder, filterRegex)
copyMatches(matches, outputFolder)
print('Done')

