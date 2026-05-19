from rich.progress import track
import time

def show_progress(steps=100, description="Processing..."):
    for _ in track(range(steps), description=description):
        time.sleep(0.01)
