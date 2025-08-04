import subprocess
import os

CREATE_NEW_CONSOLE = 0x00000010

subprocess.Popen(["uvicorn", "api.app:app", "--reload"], creationflags=CREATE_NEW_CONSOLE)
subprocess.Popen(["streamlit", "run", "dashboard/app.py"], creationflags=CREATE_NEW_CONSOLE)

print("Servers started in new console windows.")
