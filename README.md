# Tsar 👑
A system activity monitoring utility built in Python. This script tracks active Windows and logs the usage time of each application, structuring the data for later analysis.

## 🚀 About the Project
Tsar serves as a practical laboratory for exploring operating system processes and data persistence. The script runs in the background, identifies which window is in the foreground via its PID, and counts time cycles in a dictionary, securely saving the history to a JSON file upon termination.

## 🛠️ Technologies Used
*   **Python 3**
*   **Libraries:** `pywin32` (`win32gui`, `win32process`), `psutil`, `json`, `os`, `time`.

## 🧠 Technical Learnings
*   **OS Integration:** Using the Windows API to capture real-time events and processes.
*   **Data Structures:** Dynamic manipulation of nested dictionaries (`tsar_memory[process_name][window_name]`).
*   **I/O & Persistence:** Reading, creating, and writing JSON files with UTF-8 encoding.
*   **Exception Handling:** Implementation of a graceful shutdown via `KeyboardInterrupt`, ensuring in-memory data is saved to disk before killing the process.
