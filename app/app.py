from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class TaharqaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "<script>" in self.path.lower() or "or 1=1" in self.path.lower():
            with open("waf.log","a") as f:
                f.write(f"[ATTACK] {self.path} from {self.client_address[0]}\n")
            print(f"[!] Attack logged: {self.path}")

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"<h1>TAHARQA LAB - by khwajja.sec</h1><p>Try /?q = <script>alert(1)</script></p>")

print("[*] Running on http://localhost:8080 - works on any OS")
HTTPServer(("127.0.0.1",8080), TaharqaHandler).serve_forever()
