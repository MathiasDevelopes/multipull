import os

githubFolders = []

path = os.getcwd()

itemsInDir = os.listdir(path)

for item in itemsInDir:
    if os.path.isdir(item):
        if os.path.isdir(os.path.join(path, item, ".git")):
            githubFolders.append(os.path.join(path, item))

for folder in githubFolders:
    print(f"{folder}")
    os.chdir(folder)
    os.system("git pull")