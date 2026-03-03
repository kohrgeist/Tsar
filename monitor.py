import win32gui
import time
import win32process
import psutil
import json
import os


def get_active_window():
        window_id = win32gui.GetForegroundWindow()
        window_name = win32gui.GetWindowText(window_id)
        _, pid = win32process.GetWindowThreadProcessId(window_id)
        process_name = psutil.Process(pid).name()
        return window_name, process_name

def save_memory():
     with open ("tsar_memory.json", "w", encoding="utf-8") as file:
          json.dump(tsar_memory, file, indent=4, ensure_ascii=False)
          print("\nMemory saved with success!\n")


def load_memory():
    if os.path.exists("tsar_memory.json") == True:
        with open ("tsar_memory.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
         return {}
     
     
tsar_memory = load_memory()

try:
    while True:
        window_name , process_name = get_active_window()

        if process_name not in tsar_memory:
            tsar_memory[process_name] = {}

        if window_name in tsar_memory[process_name]:
            tsar_memory[process_name] [window_name] +=2

        else:        
            tsar_memory[process_name][window_name] = 2 

        time.sleep(2)

except KeyboardInterrupt:
     time.sleep(0.5)
     print("\nTurning TSAR off... Memory is being recorded in the disk.")
     time.sleep(0.75)        
     save_memory()