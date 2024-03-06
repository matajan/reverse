'''from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import datetime



con = sqlite3.connect("ips.db")
cur = con.cursor()
try:
	cur.execute("create table t_ips (time timestamp primary key, r_ip text)")                        
except sqlite3.OperationalError:
	print("Error creating DB!")                    


class RequestHandler(BaseHTTPRequestHandler):
	#def log_message(self, format, *args):
	#	pass

	def do_GET(self):
		ip = self.client_address[0]
		reversed_ip = '.'.join(reversed(ip.split('.')))
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		print(reversed_ip)
		self.wfile.write(reversed_ip.encode())
		#self.wfile.write(self.headers)


		t = datetime.datetime.now()
		cur.execute("insert into t_ips (time, r_ip) values (?, ?)", (t, reversed_ip))
		con.commit()
		return

if __name__ == '__main__':
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, RequestHandler)
	httpd.serve_forever()
	con.close()
'''

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _write_headers_to_file(self):
        with open('headers.txt', 'a') as file:
            #file.write(str(self.headers))
            file.write(str(self.headers.get('x-forwarded-for')))

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._write_headers_to_file()
        self._set_headers() 
        self.wfile.write(b'Headers were saved!')
	
    def do_POST(self):
        self.do_GET()

    def do_PUT(self):
        self.do_GET()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
