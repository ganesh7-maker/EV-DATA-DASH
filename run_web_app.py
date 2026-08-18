import http.server
import json
import os
import socket
import sys

PORT = 3000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"

LOCAL_IP = get_local_ip()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        if self.path == '/api/ip':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data = {
                "ip": LOCAL_IP,
                "port": PORT,
                "url": f"http://{LOCAL_IP}:{PORT}",
                "localhost_url": f"http://localhost:{PORT}"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        return super().do_GET()

    def log_message(self, format, *args):
        # Quiet standard logging to prevent console spam
        pass

def start_server():
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    local_url = f"http://localhost:{PORT}"
    network_url = f"http://{LOCAL_IP}:{PORT}"

    print("=" * 75)
    print(" ⚡ [EV FLEET ANALYTICS PLATFORM] - MOBILE-READY WEB SERVER LAUNCHER")
    print("=" * 75)
    print(f" 📂 Dashboard Folder : {DIRECTORY}")
    print(f" 💻 Desktop Access   : {local_url}")
    print(f" 📱 Mobile Network   : {network_url}  (Connect phone to same Wi-Fi)")
    print("=" * 75)
    print(" 💡 TIP: Open the web dashboard and click '📱 Mobile QR' in the header")
    print("        to scan the QR code directly with your phone's camera!")
    print("=" * 75)
    print(" Press Ctrl+C to stop the server.")
    print("=" * 75)
    
    server = http.server.ThreadingHTTPServer(("", PORT), CustomHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped cleanly.")

if __name__ == '__main__':
    start_server()


