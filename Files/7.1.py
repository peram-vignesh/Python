file=iput('Enter the file name')
file1=open(file)
for line in file1:
    line=upper(line)
    print (line)
