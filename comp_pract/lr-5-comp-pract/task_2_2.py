from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
from urllib.parse import unquote

from task_2_1 import write_data


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        result = ''
        with open('templates/index.html', mode='r') as html:
            result = list(map(lambda s: s.strip(), html.readlines()))
        self.wfile.write(bytes(''.join(result), "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(content_length)
        self.send_response(200)
        
        post_data = unquote(str(raw_data)).split('&')

        login = str(post_data[0].split('=')[1])
        time = str(post_data[1].split('=')[1]).replace("'",'')
        
        write_data(login + ' ' + time)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = "Form submitted!"
        self.wfile.write(response.encode('utf-8'))



httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
print('server is running ')
httpd.serve_forever()