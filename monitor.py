import win32gui
import time
import win32process
import psutil
import json
import os

def get_active_window():
    """Returns the active window's title and its process name."""
    try:
        window_id = win32gui.GetForegroundWindow()
        window_name = win32gui.GetWindowText(window_id)
        _, pid = win32process.GetWindowThreadProcessId(window_id)
        process_name = psutil.Process(pid).name()
        return window_name, process_name
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Prevents crash if the window is closed milliseconds before reading
        return "Unknown", "Unknown"

def save_memory(memory_data):
    """Saves the tracking dictionary to a local JSON file."""
    with open("tsar_memory.json", "w", encoding="utf-8") as file:
        json.dump(memory_data, file, indent=4, ensure_ascii=False)
        print("\nMemory saved with success!\n")

def load_memory():
    """Loads existing memory from JSON or returns an empty dictionary."""
    if os.path.exists("tsar_memory.json"):
        with open("tsar_memory.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def main():
    """Main execution loop."""
    tsar_memory = load_memory()
    print("Tsar is running... Press Ctrl+C to stop and save.")
    
    try:
        while True:
            window_name, process_name = get_active_window()
            
            if process_name == "Unknown":
                time.sleep(2)
                continue

            if process_name not in tsar_memory:
                tsar_memory[process_name] = {}

            if window_name in tsar_memory[process_name]:
                tsar_memory[process_name][window_name] += 2
            else:
                tsar_memory[process_name][window_name] = 2 

            time.sleep(2)

    except KeyboardInterrupt:
        time.sleep(0.5)
        print("\nTurning TSAR off... Memory is being recorded in the disk.")
        time.sleep(0.75)        
        save_memory(tsar_memory)

if __name__ == "__main__":
    main()
