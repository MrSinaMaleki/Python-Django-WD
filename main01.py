

from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import

index_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Maktab 112</title>
    <script src="https://cdn.tailwindcss.com"></script>

</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>


"""


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(index_content, 'utf-8'))
    

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8008

    server = HTTPServer((host, port), Server)
    print(f"http://{host}:{port}")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        pass

    finally:
        server.server_close()
