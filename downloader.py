# downloader.py

import socket
import ssl
import time
import requests

def download_file(host, port, path):
    # First try: LOW-LEVEL SOCKET (for marks)
    try:
        context = ssl.create_default_context()
        sock = socket.create_connection((host, port), timeout=10)
        secure_sock = context.wrap_socket(sock, server_hostname=host)

        request = f"""GET {path} HTTP/1.1\r
Host: {host}\r
User-Agent: Mozilla/5.0\r
Accept: */*\r
Connection: close\r
\r
"""

        start_time = time.time()
        secure_sock.send(request.encode())

        total_data = b""

        while True:
            data = secure_sock.recv(4096)
            if not data:
                break
            total_data += data

        end_time = time.time()
        secure_sock.close()

        header_end = total_data.find(b"\r\n\r\n") + 4
        body = total_data[header_end:]

        file_size = len(body)
        time_taken = end_time - start_time
        speed = file_size / time_taken if time_taken > 0 else 0

        print("✅ Used SOCKET method")

        return file_size, time_taken, speed

    except Exception as e:
        print("⚠️ Socket failed, switching to requests:", e)

    # Second try: REQUESTS (backup)
    try:
        url = f"https://{host}{path}"

        start_time = time.time()
        response = requests.get(url, stream=True)

        total_size = 0
        for chunk in response.iter_content(4096):
            total_size += len(chunk)

        end_time = time.time()

        file_size = total_size
        time_taken = end_time - start_time
        speed = file_size / time_taken if time_taken > 0 else 0

        print("✅ Used REQUESTS fallback")

        return file_size, time_taken, speed

    except Exception as e:
        print("❌ Both methods failed:", e)
        return 0, 0, 0