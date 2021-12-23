#!/usr/bin/env python3
import os

#Sets the current working directory, but if custom_dir_path is specified and valid, it will be overwritten with custom path.
path = os.getcwd()

# Checks if the user wants to choose a custom directory.
custom_dir_choice = input("Would you like to specify a custom dir (y/n): ").lower()
if custom_dir_choice == "y":
    custom_dir_path = input("Enter the custom directory path: ")
    if os.path.isdir(custom_dir_path):
        path = custom_dir_path
    else:
        print("Directory not valid, falling back to current working directory.")


# Puts all folders within the path with sub-folder .git into a list.
githubFolders = [os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item, ".git"))]

#Checks if there are no github folders in the path directory.
if len(githubFolders) == 0:
    print("There are no github folders in this directory, quitting.")
    exit(0)

# Iterates through every folder from the githubFolders list, and executes the git pull comamnd on them.
for folder in githubFolders:
    print(f"Executing git pull on {folder}")
    os.chdir(folder)
    os.system("git pull")