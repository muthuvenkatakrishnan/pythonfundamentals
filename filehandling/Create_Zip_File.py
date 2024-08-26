import os
from zipfile import ZipFile
os.chdir("D:/Python-June-1to3Batch/Os_Module")
#get the files from a directory and store it in path []
def get_paths(folder):
    
    paths = []
    for root, directories, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return paths

directory = "./assets"
paths = get_paths(directory)
print("Zipping the files in the given directory")
zip = ZipFile('assets.zip','w')
for file in paths:
        zip.write(file)
print("Zipping completed")