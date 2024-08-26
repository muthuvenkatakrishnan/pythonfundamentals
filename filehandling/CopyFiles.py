# import os
# print(os.getcwd())
# os.chdir('D:/Python-June-1to3Batch/filehandling/alpha')
# os.popen('copy resume.txt cv.txt')
# os.system('copy cv.txt res.txt')

# Using Threading and Shutil
# import shutil
# from threading  import Thread
# Thread(target=shutil.copy, args=['res.txt', 'my_res.txt']).start()

# Using Subprocess
# import subprocess
# status = subprocess.call('copy my_res.txt your_res.txt', shell=True)
# if status !=0:
#     if status <0:
#         print(f'The process is killed {status}')
#     else:
#         print(f'The process is terminated with error {status}')
# else:
#     print('The process is completed successfully')


# using Shutil copyfile method
# import shutil
# shutil.copyfile('cv.txt', 'test1.txt')

# # using Shutil copy method
# shutil.copy('cv.txt', 'test2.txt')

# # using Shutil copy2 method
# shutil.copy2('cv.txt', 'test3.txt')

# # using Shutil copyfileobj method
# f_file = open('cv.txt', 'rb')
# s_file = open('test4.txt', 'wb')
# shutil.copyfileobj(f_file, s_file)\

# Copy all the files in the Alpha directory to the Beta directory

import os
import shutil

source_folder = r"D:\Python-June-1to3Batch\filehandling\alpha\\"
destination_folder = r"D:\Python-June-1to3Batch\filehandling\beta\\"

for file_name in os.listdir(source_folder):
    source = source_folder + file_name
    destination = destination_folder + file_name

    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)

# write a menu driven python code that gives two options as follows:
# 1. Copy a file content
# 2. Copy the file from one directory to another directory
# 3. Exit

# If the user selects option 1, 
# then the program should ask the user to enter the file name and the content to be written to the file.

# If the user selects option 2,
# then the program should ask the user to enter the source directory and the destination directory 
# to copy the file.

# If the user selects option 3, then the program should exit.

# If the user selects any other option, then the program should display an error message.

