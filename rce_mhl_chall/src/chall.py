from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs, unquote
import logging,mmap,subprocess,re,sys

html = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
<form action="" method="POST">
 <label> My first name</label>
 <input type="text" id="Name" name="first"><br><br>
 <label> My last name</label>
 <input type="text" id="last" name="last"><br><br>
 <input type="submit" value="Submit">
</form>
  </body>
</html>
"""
nope = """
<script>
<!--
var s="=dfoufs?=jnh!tsd>iuuqt;00kvtuivnbo{/nf0514/kqh!bmu>?=cs?op!qjqfmjof!;)!=0dfoufs?";
m=""; for (i=0; i<s.length; i++) m+=String.fromCharCode(s.charCodeAt(i)-1); document.write(m);
//-->
</script>
"""

err = """
<script>
<!--
var s="=dfoufs?=jnh!tsd>iuuqt;00kvtuivnbo{/nf0611/kqh!bmu>?=cs?!tpnfuijoh!fssps!;)=0dfoufs?";
m=""; for (i=0; i<s.length; i++) m+=String.fromCharCode(s.charCodeAt(i)-1); document.write(m);
//-->
</script>
"""

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_response_text(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

    def do_GET(self):
        if re.search(r"\/solver", self.path):
            self._set_response_text()
            solver = open("solver.txt", "r")
            for line in solver:
                self.wfile.write(line.encode())
        elif re.search(r"\/robots.txt", self.path):
            self._set_response_text()
            robots = "User-agent: *\n/chall.py"
            self.wfile.write(robots.encode())
        elif re.search(r"\/chall.py", self.path):
            self._set_response_text()
            try:
                self.wfile.write(subprocess.check_output(f"cat {unquote(self.path[1:])}", shell=True,executable='/bin/bash',stderr=subprocess.PIPE))
            except subprocess.CalledProcessError as e:
                self.wfile.write(str(e).encode())
        else:
            self._set_response()
            self.wfile.write(html.encode())

    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile.decode("utf-8"), pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(self.rfile.read(length).decode("utf-8"),keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_POST(self):
        postvars = self.parse_POST()
        str1 = ''.join(postvars['first'])+" "+''.join(postvars['last'])
        print(str1)
        cmd = "echo "+str1+" | toilet --html --metal"
        if re.search(r"\&|\||\>|\<|\;|\$|\(|\)", str1):
            if re.search(r"\$", str1):
                if re.search(r"\$", str1) and re.search(r"\>", str1):
                    self.hav(cmd)
                else:
                    self.hav(cmd)
            else:
                self._set_response()
                self.wfile.write(nope.encode())
        else:
            self.hav(cmd)

    def hav(self,cmd):
        try:
            sh3ll = subprocess.check_output(cmd, shell=True,executable='/bin/bash',stderr=subprocess.PIPE)
            self._set_response()
            self.wfile.write(b"My name is "+sh3ll)
        except subprocess.CalledProcessError as ee:
            self._set_response()
            self.wfile.write(err.encode())
            self.wfile.write(str(ee).encode())

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.DEBUG)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
