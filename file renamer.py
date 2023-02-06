import os

def rename_files(directory, new_name, extension):
    for count, filename in enumerate(os.listdir(directory)):
        dst = new_name + str(count) + extension
        src = directory + '/' + filename
        dst = directory + '/' + dst

        os.rename(src, dst)

directory = input("Enter the directory path: ")
new_name = input("Enter the new name for the files: ")
extension = input("Enter the extension of the files: ")
rename_files(directory, new_name, extension)

print("Files renamed successfully!")
