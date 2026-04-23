import psutil
import time

def monitor():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

if __name__ == "__main__":
    while True:
        monitor()
        time.sleep(5)