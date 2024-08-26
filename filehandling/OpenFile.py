data = open("D:/Python-June-1to3Batch/filehandling/charlie/cv.txt",'r')

#print(data.read()) # reads the entire file
#print(data.read(5)) # reads the first 5 characters
#print(data.readlines())# reads the file line by line

# iterating over the file using for loop:

for lines in data:
    print(lines, end='')