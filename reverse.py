from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import datetime



con = sqlite3.connect("ips.db")
cur = con.cursor()
try:
	cur.execute("create table t_ips (time timestamp primary key, r_ip text)")                        
except sqlite3.OperationalError:
	print("Error creating DB!")                    


class RequestHandler(BaseHTTPRequestHandler):
	def log_message(self, format, *args):
		pass

	def do_GET(self):
		ip = self.client_address[0]
		reversed_ip = '.'.join(reversed(ip.split('.')))
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		print(reversed_ip)
		#self.wfile.write(reversed_ip.encode())
		self.wfile.write(self.headers)

		
		t = datetime.datetime.now()
		cur.execute("insert into t_ips (time, r_ip) values (?, ?)", (t, reversed_ip))
		con.commit()
		return

if __name__ == '__main__':
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, RequestHandler)
	httpd.serve_forever()
	con.close()
#
