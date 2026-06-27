import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print(f"--- Local Web Server ---")
print(f"Serving at: http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")