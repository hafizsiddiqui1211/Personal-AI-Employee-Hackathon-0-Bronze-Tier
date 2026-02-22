from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil
import time

VAULT = Path("AI_Employee_Vault")
NEEDS_ACTION = VAULT / "Needs_Action"
INBOX = VAULT / "Inbox"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        src = Path(event.src_path)
        dest = NEEDS_ACTION / src.name
        shutil.move(src, dest)
        print(f"Moved {src.name} to Needs_Action")

observer = Observer()
observer.schedule(Handler(), path=str(INBOX), recursive=False)
observer.start()

print("Filesystem Watcher running...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()