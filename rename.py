import os

path = r'E:/吴军·硅谷来信'
str = r'吴军'
pos = 21
os.chdir(path)
file_list = os.listdir(path)

print(file_list )

for filename in file_list:

    if str in filename:
        print(filename[pos:])
        new_name = filename[pos:]
        os.rename(filename, new_name)

print(file_list )