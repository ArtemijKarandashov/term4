from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        
        login = '1149920'
        dt = datetime.now()

        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        result = login + ',' + str(dt)
        self.wfile.write(bytes(result, "utf-8"))


httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
print('server is running ')
httpd.serve_forever()