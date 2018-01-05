from scipy.io import loadmat
import pandas as pd

matrix = loadmat("../cars_annos.mat")

# create as many directories as the number of classes in dataset (196)
import os
for idx in range(matrix['class_names'].shape[1]):
    os.makedirs("./"+str(idx+1))

# take out class numbers and class names from annotations
classNumber=[]
className=[]
for idx in range(matrix['annotations'].shape[1]):
    classNumber.append(matrix['annotations'][0][idx][5][0][0]) # index 5 has class number
    className.append(matrix['annotations'][0][idx][0][0]) # index 0 has the class name

# use the class name to fetch file from source directory and copy it in corresponding class number directory
import shutil
for idx, _ in enumerate(classNumber):
    shutil.copy2('../'+className[idx],'./'+str(classNumber[idx]))

# rename each directory from class number to actual class name
import os
for idx, _ in enumerate(classNumber):
    if os.path.exists(str(classNumber[idx])):
        os.rename(str(classNumber[idx]),matrix['class_names'][0][classNumber[idx]-1][0])
