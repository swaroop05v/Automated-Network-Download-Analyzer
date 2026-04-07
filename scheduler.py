# scheduler.py

import time
from downloader import download_file
from logger import log_data

# Stable server
HOST = "speed.cloudflare.com"
PORT = 443
PATH = "/__down?bytes=5000000"

def run():
    try:
        file_size, time_taken, speed = download_file(HOST, PORT, PATH)

        speed_mb = speed / (1024 * 1024)

        print(f"Downloaded: {file_size} bytes")
        print(f"Time: {time_taken:.2f} sec")
        print(f"Speed: {speed_mb:.2f} MB/s")

        log_data(file_size, time_taken, speed_mb)

    except Exception as e:
        print("Error:", e)

i = 0
while(1):
    print(f"\nRun {i+1}")
    i += 1
    run()

    time.sleep(5)  # 1 minute (change to 3600 for real)