import os
import shutil

desktop_abs_path = "/Users/marcpartensky/Desktop"
images_abs_path = "/Users/marcpartensky/Pictures/Images"
files = os.listdir(desktop_abs_path)

captures = []

for file in files:
    if file.startswith('Capture'):
        captures.append(file)

while len(captures)>0:
    source = os.path.join(desktop_abs_path, captures[0])
    destination = os.path.join(images_abs_path, captures[0])
    shutil.move(source, destination)
    del captures[0]

