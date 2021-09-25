from http.server import BaseHTTPRequestHandler, HTTPServer


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        path = self.path
        if path == '/':
            path = '/index'

        try:
            file = open("pages" + path + ".html", 'r')
        except FileNotFoundError:
            file = open("pages/404.html", 'r')

        mess = file.read()
        file.close()
        self.wfile.write(bytes(mess, "utf8"))
        return


print('START SERVER SESSION')
server_adress = ('127.0.0.1', 8081)
server = HTTPServer(server_adress, myHandler)
server.serve_forever()

