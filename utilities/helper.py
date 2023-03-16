import json
import os
import pyautogui

def return_create_record():
    rootpath=os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(_file_))))
    with open(rootpath+"\\TestData\\create_data.json") as f:
        data=json.load(f)
    return data

def return_update_record():
    rootpath=os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(_file_))))
    with open(rootpath+"\\TestData\\update_data.json") as f:
        data=json.load(f)
    return data