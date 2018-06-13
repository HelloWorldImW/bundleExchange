
import os

for parent,dirnames,filenames in os.walk('./bundle'):
    for filename in filenames:
        print ("parent is:" + parent)
        print ("filename is:" + filename)
        os.system("cp "+os.path.join(parent,filename)+" ./source/"+filename)
