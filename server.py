
import os
import socket
import threading

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8765"))

def handle_client(conn, addr):
    print(f"TCP connection from {addr}")
    try:
        with conn:
            conn.settimeout(30)
            data = conn.recv(4096)

            if data:
                print(f"Received {len(data)} bytes: {data!r}")
                conn.sendall(b"OK: TCP data received\n")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        print(f"Disconnected: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(20)

print(f"TCP server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_client,
        args=(conn, addr),
        daemon=True
    ).start()
