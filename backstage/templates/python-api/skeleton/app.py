from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200); self.end_headers(); self.wfile.write(b'ok'); return
        self.send_response(200); self.end_headers(); self.wfile.write(b'hello from ${{ values.component_id }}')

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
