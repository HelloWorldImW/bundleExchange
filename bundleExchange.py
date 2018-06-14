
import os

def strchr(sStr1,sStr2):
    a = 0
    try:
        nPos = sStr1.index(sStr2)
        a = nPos
    except:
        a = -1
    return a

def getFileName(path,fileName):
    fPath =  os.path.split(path)[-1]
    fPath = os.path.splitext(fPath)[0]
    fName = os.path.splitext(fileName)[0]
    suffix = os.path.splitext(fileName)[1]
    if suffix != '.png':
        return -1
    if strchr(os.path.splitext(fileName)[0],'@2x') == -1 and strchr(os.path.splitext(fileName)[0],'@3x') ==-1:
        fPath = os.path.splitext(fileName)[0]+'@2x.png'
    elif strchr(os.path.splitext(fileName)[0],'@2x'):
        fPath = fPath+'@2x.png'
    elif strchr(os.path.splitext(fileName)[0],'@3x'):
        fPath = fPath+'@3x.png'
    return fPath

def exchangeBundle(sourcePath,targetPath):
    for parent,dirnames,filenames in os.walk('./asset'):
        for file in filenames:
            fileName = getFileName(parent,file)
            if fileName != -1:
                print (fileName)
                os.system("cp "+os.path.join(parent,file)+" ./bundle/"+fileName)

exchangeBundle('./asset','./bundle')
