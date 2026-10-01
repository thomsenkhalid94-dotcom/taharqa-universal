import socket
print("--- TAHARQA SCANNER  by.khwajja.sec ---")
target = "127.0.0.1"
for port in [22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        print(f"[OPEN] {port}")
    except:
        print(f"[CLOSED] {port}")
    s.close()
print("                                       ")
print("========================*khwajja.sec®*=")
