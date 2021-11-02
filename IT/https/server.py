from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


httpd = HTTPServer(('10.0.0.2', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="server.key", 
        certfile="server.crt", server_side=True)

httpd.serve_forever()
