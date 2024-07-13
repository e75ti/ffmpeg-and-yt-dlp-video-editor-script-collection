# Requires exiftool added to path
# WIP Alpha version, will improve

import tkinter as tk
import tkinter.filedialog as fd
import os
import pytz
from datetime import datetime

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

def printintro():
    print("1. Choose files\n2. Display files in library\n3. Start rendering\n4. Clear files list\ne. Exit")

def ffmpeg(file):
    command = 'ffmpeg -i "' + str(file) + '" -c:v libx264 -crf 24 -preset medium -tune film -profile:v high -acodec aac -strict -2 -b:a 384k -map_metadata 0 -movflags use_metadata_tags "' + str(os.path.splitext(file)[0]) + '-temp.MP4'
    return command

def is_dst(dt=None, timezone="Etc/GMT+2"): # Adjust to your local timezone
    if dt is None:
        dt = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0
    
def getmtime(file_path):
    return os.path.getmtime(file_path)

print("Video losless filesize reducer!\n")
full_list = []
while 1:
    printintro()
    entry = input()
    if entry == "1":
        print("Choose files!")
        files = fd.askopenfilenames(parent=root, title='Choose files')   
        for file in files:
            full_list.append(file)
    elif entry == "2":
        print(full_list)
    elif entry == "3":
        print("Starting rendering!")
        res = []
        for i in full_list:
            if i not in res:
                res.append(i)
        print(res)
        for all_files in res:
            print(ffmpeg(all_files))
        question = input("Do you want to run ffmpeg? y/n\n")
        if question == "y":
            textfile = open("reduced_list.log", "a")
            for all_files in res:
                os.system('cmd /c ' + str(ffmpeg(all_files)))
                os.system('cmd /c ' + 'exiftool -TagsFromFile "' + str(all_files) + '" "-FileModifyDate<filemodifydate" "' + str(os.path.splitext(all_files)[0]) + '-temp.MP4"')
                os.remove(str(all_files))
                os.rename(str(os.path.splitext(all_files)[0]) + "-temp.mp4",str(os.path.splitext(all_files)[0]) + ".MP4")
                textfile.write(str(all_files) + "\n")
            textfile.close()
    elif entry == "4":
        full_list = []
    elif entry == "e":
        break
    else:
        print("Wrong input\n")

root.destroy()
