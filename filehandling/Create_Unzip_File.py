from zipfile import ZipFile
import os
os.chdir("D:/Python-June-1to3Batch/Os_Module")
file = "assets.zip"
zip = ZipFile(file,'r')
zip.extractall()
print("Unzipping completed")