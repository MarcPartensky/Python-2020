import os
import sys


def webtojpg():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.webp'):
            name = file[:-5]
            print(f"ffmpeg -i '{file}' '{name}.jpg'")
            os.system(f"ffmpeg -i '{file}' '{name}.jpg'")

def jpgtomp3():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.jpg'):
            print(file)
            name = file[:-4]
            print(f"ffmpeg -i '{name}.mp3' -i '{name}.jpg' -map_metadata 0 \
-map 0 -map 1 -acodec copy '{name}.mp3'")
            os.system(f"ffmpeg -i '{name}.mp3' -i '{name}.jpg' -map_metadata 0 \
-map 0 -map 1 -acodec copy '{name}.tempo.mp3'")

def rename():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.tempo.mp3'):
            name = file[:-len('.tempo.mp3')]
            os.rename(f"{name}.tempo.mp3", f"{name}.mp3")


def clean_temp():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.temp.mp3'):
            os.remove(file)

def clean_jpg():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.jpg'):
            os.remove(file)

def clean_webp():
    for file in os.listdir(os.getcwd()):
        if file.endswith('.webp'):
            os.remove(file)

def clean():
    clean_jpg()
    clean_temp()
    clean_webp()

if 'webptojpg' in sys.argv:
    webtojpg()

if 'jpgtomp3' in sys.argv:
    jpgtomp3()

if 'rename' in sys.argv:
    rename()

if 'clean' in sys.argv:
    clean()

if 'clean-jpg' in sys.argv:
    clean_jpg()

if 'clean-temp' in sys.argv:
    clean_temp()

if 'clean-webp' in sys.argv:
    clean_webp()

if len(sys.argv)==1:
    webtojpg()
    jpgtomp3()
    rename()
    clean()

