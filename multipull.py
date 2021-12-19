import os

# Gets the current working directory
path = os.getcwd()


#Returns all items in the current working directory 
itemsInDir = os.listdir(path)

# Puts all folders with sub-folder .git into a list.
githubFolders = [os.path.join(path, item) for item in itemsInDir if os.path.isdir(os.path.join(path, item, ".git"))]

# Iterates through every github folder from the githubFolders list, and executes git pull comamnd on them.
for folder in githubFolders:
    print(f"Executing git pull on {folder}")
    os.chdir(folder)
    os.system("git pull")