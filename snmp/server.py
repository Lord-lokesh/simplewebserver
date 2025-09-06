from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
   <head>
   </head>
   <body bgcolor="red">
        <table border ="5" align="center" bgcolor="pink" cellpadding="10"
        <caption><h1>List of protocols </h1></caption>
        <tr><th>s.no</th><th>Name of the Layer </th>
            <th>Name of the protocols</th>
        </tr>
        <tr>
            <td>1</td><td>Appalication Layer </td><td>HTTP,FTP</td>
        </tr>
        <tr>
            <td>2</td><td>Transport Layer </td><td>TCP &UDP</td>
        </tr>
        <tr>
            <td>3</td><td>Internal Layer</td><td>ICMP,ARP,IGMP</td>
        </tr>
        <TR>
            <td>4</td><td>Network access Layer</td><td>TCP&UPD</td>
        </TR>
    </table>    
   </body>
</html>

-'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()