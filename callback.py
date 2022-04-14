import os
import subprocess
from pathlib import Path

import image_pytesseract
import re

def ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)

def get_exp(log):
    last_exp = ''

    try:
        last_exp = list(filter(lambda f: "Results saved to" in f, log.split("\n")))[0].split("/")[-1]
    except:
        print('Error get exp')
    
    return last_exp



#receive a dir with images and identify the cards

#func to detect the next folder
target_image_folder = '/home/yoshi/Pictures/cards'

root_dir = "/home/yoshi/Apps/yolov5/runs/detect/"
next_run = ''

# check folder
if os.path.exists(target_image_folder):
    for file in os.listdir(target_image_folder):
        current_image = os.path.join(target_image_folder, file)

        card_name = ''
        edition = ''

        result = subprocess.run("python /home/yoshi/Apps/yolov5/detect.py --weights /home/yoshi/Apps/yolov5/runs/detect/khm_name.pt --source " + current_image + " --save-crop --save-txt", 
                shell=True,
                capture_output=True,
                text=True)

        result_dir = os.path.join("/home/yoshi/Apps/yolov5/runs/detect/", ansi(get_exp(result.stderr)))
        result_crop_dir = os.path.join(result_dir, 'crops')
        result_labels_dir = os.path.join(result_dir, 'labels')
        result_name = os.path.join(result_crop_dir, 'Name')

        if os.path.exists(result_labels_dir):
            if len(os.listdir(result_labels_dir)) > 0:
                with open(os.path.join(result_labels_dir, os.listdir(result_labels_dir)[0])) as file:
                    line = file.readlines()
                    print(line)
            else:
                print('Nothing was detected')

        if os.path.exists(result_name):
            if len(os.listdir(result_name)) > 0:
                card_name = image_pytesseract.run(os.path.join(result_name, os.listdir(result_name)[-1]))
                print(card_name)
        else:
            print('None image was found')
else:
    print('Path doesnt exist')
    

# print("stdout:", result.stdout)
# print("stdout:", result.stderr)
# print("return code: ", result.returncode)

#get last run
# if os.path.exists(root_dir):
#     last_run_id = 'ext' + str(int(str(sorted(Path(root_dir).iterdir(), key=os.path.getmtime)[-1]).split('/')[-1].replace('exp', '')) + 1)
#     next_run = os.path.join(root_dir, last_run_id)
#     print(next_run)