import requests
import json
import os
import git
import shutil
from config import apikeys

filename = "repos-private.json"

#url = 'https://github.com/GabrielaDomiciano/private'
url = 'https://api.github.com/repos/GabrielaDomiciano/private'


#apikey='config.py'


repo_clone_url = f'https://{apikeys["htmltopdfkey"]}@github.com/GabrielaDomiciano/private.git'
clone_dir = "private"
file_to_edit = "andrew_replace.txt"  # file name that has "Andrew"

# Access repository information
response = requests.get(url, auth=(apikeys["htmltopdfkey"], ""))

print("Request status:", response.status_code)

with open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)



# Clone the repository
if os.path.exists(clone_dir):
    import shutil
    shutil.rmtree(clone_dir)    


print("Cloning private repository...")
repo = git.Repo.clone_from(repo_clone_url, clone_dir)

#  Modify the file
file_path = os.path.join(clone_dir, file_to_edit)

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace "Andrew" with my name
new_content = content.replace("Andrew", "Gabriela")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(new_content)

print(f"Modifications made to the file {file_to_edit}.")

# Commit and push
repo.git.add(file_to_edit)
repo.index.commit("Replace 'Andrew' with 'Gabriela' in the file")

origin = repo.remote(name='origin')
origin.push()

print("Changes pushed successfully.")
print("Cloned directory contents:")
print(os.listdir(clone_dir)) 









