# using Shutil copyfile method
import shutil
import os
def copyFiles(src_file, dest_file):
    shutil.copyfile(src_file, dest_file)

def copyFilesDir(src_dir, dest_dir):
    for file_name in os.listdir(src_dir):
        source = r'src_dir' + file_name
        destination = r'dest_dir' + file_name

        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)

# menu driven code

while True:
    print("1. Copy a file content")
    print("2. Copy the file from one directory to another directory")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        src_file = input("Enter the source file: ")
        dest_file = input("Enter the destination file: ")
        copyFiles(src_file, dest_file)
    elif choice == 2:
        src_dir = input("Enter the source directory: ")
        dest_dir = input("Enter the destination directory: ")
        copyFilesDir(src_dir, dest_dir)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
