import os

# Specify the directory you want to list
directory_path = '/'  # '.' refers to the current working directory

# Get the list of files and directories in the specified path
directory_content = os.listdir(directory_path)

# Print the contents of the directory
for item in directory_content:
    print(item)
