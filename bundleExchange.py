
import os

def strchr(sStr1,sStr2):
    a = 0
    try:
        nPos = sStr1.index(sStr2)
        a = nPos
    except:
        a = -1
    return a

for parent,dirnames,filenames in os.walk('./bundle'):
    for filename in filenames:
        expName = ''
        needApped = False
        if strchr(os.path.splitext(filename)[0],'@2x') == -1 and strchr(os.path.splitext(filename)[0],'@3x') ==-1 :
            needApped = True
        if needApped:
            expName = os.path.splitext(filename)[0]+'@2x'+os.path.splitext(filename)[1]
        os.system("cp "+os.path.join(parent,filename)+" ./source/"+expName)
