# logger.py

import csv
from datetime import datetime

FILE_NAME = "log.csv"

def log_data(file_size, time_taken, speed):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            file_size,
            round(time_taken, 3),
            round(speed, 2)
        ])