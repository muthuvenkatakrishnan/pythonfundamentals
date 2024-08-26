import os, sys
os.chdir('D:/Python-June-1to3Batch/Os_Module/assets')
# os.rename('asset_list.txt', 'asset_list_new.txt')

# import shutil
# for i in range(6):
#     shutil.copy('asset_list_new.txt', f'asset_list_{i+1}.txt')

# to rename multiple files in a directory
i = 1
for file in os.listdir():
    src = file
    destn = "my_file" + str(i) + ".docx"
    os.rename(src, destn)
    i += 1