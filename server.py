import string
import cgi
import time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.lower().endswith(".json"):
                f = open(curdir + sep + self.path)

                self.send_response(200)
                self.send_header('Content-type',    'application/json')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()
