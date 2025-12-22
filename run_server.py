#!/usr/bin/env python3
"""
run_local.py
Serve the current project directory over HTTP with permissive CORS headers
and open the default browser to the app's `index.html` page.

Usage example:
    python run_local.py --port 8000 --dir "d:/Projects/Promotions web app"

This is intentionally lightweight and requires Python 3.7+.
"""

import argparse
import os
import webbrowser
from http.server import SimpleHTTPRequestHandler
import socketserver
import urllib.request
import urllib.parse
import io
import traceback
import socket
import threading
import time
import subprocess
import sys


class CORSRequestHandler(SimpleHTTPRequestHandler):
    """Simple HTTP handler that adds CORS headers to responses."""
    def end_headers(self):
        # Allow cross-origin requests (helpful when testing fetch/XHR in the browser)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS,HEAD')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def _proxy_forward(self, target_url):
        """Forward the current request to target_url and stream response back to client."""
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length) if length > 0 else None

            req = urllib.request.Request(target_url, data=body, method=self.command)
            # Copy selected headers
            for h in ('Content-Type', 'User-Agent', 'Accept'):
                if h in self.headers:
                    req.add_header(h, self.headers[h])

            with urllib.request.urlopen(req, timeout=15) as resp:
                status = resp.getcode()
                data = resp.read()
                self.send_response(status)
                # Copy response headers (but do not copy transfer-encoding)
                for k, v in resp.getheaders():
                    if k.lower() == 'transfer-encoding':
                        continue
                    self.send_header(k, v)
                # Ensure CORS
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            # Log full traceback to server console for easier diagnosis
            print('Proxy forwarding exception:')
            traceback.print_exc()
            self.send_response(502)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            msg = f'Proxy error: {e}\nSee server console for details.'.encode('utf-8')
            self.wfile.write(msg)

    def do_POST(self):
        # Proxy endpoint for local development
        if self.path.startswith('/proxy'):
            # forward to configured Apps Script URL
            # You can set APPSCRIPT_URL environment variable or edit below
            target = os.environ.get('APPSCRIPT_URL') or 'https://script.google.com/macros/s/AKfycbzgf6NXFQoIPWlw7Py2TmzFo0DuQD1mci1QfgFAL8eN4wE7N8b3LFBO2gmKqE46Gt07/exec'
            # If the path contains a suffix, append it
            # e.g. /proxy?action=register -> forward as is
            if self.path != '/proxy' and self.path.startswith('/proxy'):
                qs = self.path[len('/proxy'):]
                target = target + qs
            return self._proxy_forward(target)
        # otherwise, fallback to normal static handling (not expected)
        return super().do_POST()

    def do_GET(self):
        # Special shutdown path for graceful restart: calling this will cause the server to shutdown
        if self.path == '/__run_local_shutdown__':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'OK')
            # Shutdown in separate thread to avoid blocking current request handling
            def _shutdown_server():
                try:
                    # give the response a moment to flush
                    time.sleep(0.1)
                    self.server.shutdown()
                except Exception:
                    pass
            threading.Thread(target=_shutdown_server, daemon=True).start()
            return
        # Diagnostic endpoint to test server -> Apps Script connectivity
        if self.path == '/proxy_test':
            target = os.environ.get('APPSCRIPT_URL') or 'https://script.google.com/macros/s/AKfycbzgf6NXFQoIPWlw7Py2TmzFo0DuQD1mci1QfgFAL8eN4wE7N8b3LFBO2gmKqE46Gt07/exec?action=getLeaderboard'
            try:
                with urllib.request.urlopen(target, timeout=10) as resp:
                    data = resp.read()
                    self.send_response(200)
                    self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(data)
                    return
            except Exception as e:
                print('Proxy test failed:')
                traceback.print_exc()
                self.send_response(502)
                self.send_header('Content-Type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(f'Proxy test error: {e}\nSee server console for details.'.encode('utf-8'))
                return
        if self.path.startswith('/proxy'):
            target = os.environ.get('APPSCRIPT_URL') or 'https://script.google.com/macros/s/AKfycbzgf6NXFQoIPWlw7Py2TmzFo0DuQD1mci1QfgFAL8eN4wE7N8b3LFBO2gmKqE46Gt07/exec'
            if self.path != '/proxy' and self.path.startswith('/proxy'):
                qs = self.path[len('/proxy'):]
                target = target + qs
            return self._proxy_forward(target)
        return super().do_GET()


def run(port: int, directory: str, open_browser_flag: bool = True):
    # Change to the target directory so SimpleHTTPRequestHandler serves files from there
    os.chdir(directory)
    proxy_proc = None
    # Optionally auto-start proxy_server.py (if present) to handle API requests locally
    def _start_proxy_if_available():
        nonlocal proxy_proc
        # Allow disabling via environment variable
        if os.environ.get('PROXY_DISABLED', '').lower() in ('1', 'true', 'yes'):
            print('Proxy auto-start disabled via PROXY_DISABLED')
            return
        proxy_path = os.path.join(directory, 'proxy_server.py')
        if not os.path.isfile(proxy_path):
            # No proxy file present
            return
        try:
            python_exec = sys.executable or 'python'
            # Start proxy as a detached process; inherit env to pass JSONBIN_MASTER_KEY, ADMIN_PASSWORD, etc.
            env = os.environ.copy()
            proxy_proc = subprocess.Popen([python_exec, proxy_path], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f'Started proxy server (pid={proxy_proc.pid})')
        except Exception as e:
            print('Failed to start proxy server:', e)

    def _stop_proxy_if_started():
        nonlocal proxy_proc
        try:
            if proxy_proc and proxy_proc.poll() is None:
                print('Stopping proxy server...')
                proxy_proc.terminate()
                try:
                    proxy_proc.wait(timeout=3)
                except Exception:
                    proxy_proc.kill()
        except Exception as e:
            print('Error stopping proxy server:', e)
    handler = CORSRequestHandler
    # Attempt to politely ask an existing run_local server to shutdown (if it was running here before)
    try:
        shutdown_url = f'http://localhost:{port}/__run_local_shutdown__'
        urllib.request.urlopen(shutdown_url, timeout=1)
        print('Requested existing local server to shut down...')
        # give it a moment to stop
        time.sleep(0.5)
    except Exception:
        # no existing server responded
        pass

    # Use a threading TCPServer and allow address reuse to reduce "address already in use" issues
    class ThreadingTCPServer(socketserver.ThreadingTCPServer):
        allow_reuse_address = True

    # Try to bind to the requested port; if it fails (permission or in-use), try a small range of ports
    httpd = None
    tried_ports = []
    for p in range(port, port + 11):
        tried_ports.append(p)
        try:
            httpd = ThreadingTCPServer(("", p), handler)
            port = p
            break
        except PermissionError as e:
            print(f"PermissionError: cannot bind to port {p}: {e}")
            continue
        except OSError as e:
            print(f"OS error binding to port {p}: {e}")
            continue

    if httpd is None:
        print(f"Failed to bind to any port in the range {tried_ports}.")
        print("Possible causes: another process is using the port, firewall/AV blocking, or insufficient permissions.")
        print("On Windows, run 'netstat -aon | findstr :<port>' to find the process holding the port, then 'taskkill /PID <pid> /F' to stop it, or run this script as Administrator.")
        return

    with httpd as server:
        url = f'http://localhost:{port}/index.html'
        print(f"Serving directory: {os.path.abspath(directory)}")
        print(f"Open this URL in your browser: {url}")
        # Try to start local proxy (for development) before opening browser
        _start_proxy_if_available()
        if open_browser_flag:
            try:
                webbrowser.open(url)
            except Exception as e:
                print('Could not open browser automatically:', e)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nShutting down server...')
            httpd.server_close()
            # Stop proxy if we started it
            try:
                _stop_proxy_if_started()
            except Exception:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serve this project locally and open index.html')
    parser.add_argument('--port', '-p', type=int, default=4000, help='Port to listen on (default: 8000)')
    parser.add_argument('--dir', '-d', default='.', help='Directory to serve (default: current directory)')
    parser.add_argument('--no-open', action='store_true', help="Don't open the browser automatically")

    args = parser.parse_args()
    run(args.port, args.dir, not args.no_open)
