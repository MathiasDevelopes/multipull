#!/usr/bin/env python3
import os

# Gets the current working directory
path = os.getcwd()

# Puts all folders within the current directory with sub-folder .git into a list.
githubFolders = [os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item, ".git"))]

# Iterates through every github folder from the githubFolders list, and executes git pull comamnd on them.
for folder in githubFolders:
    print(f"Executing git pull on {folder}")
    os.chdir(folder)
    os.system("git pull")