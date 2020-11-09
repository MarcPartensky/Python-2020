#!/usr/bin/env python -m httpserver 8000
import http.server
import socketserver

PORT = 80

server = http.server.HTTPServer
Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ["/"]

with server(("", PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()
