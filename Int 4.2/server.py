from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Проверяем путь запроса
        if self.path == '/healthz':
            self.send_response(200)  # Отправляем статус 200 OK
            self.end_headers()
        else:
            self.send_response(404)  # Если путь не совпадает, отправляем 404 Not Found
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('',80)  # Запуск на порту 80
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 80...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
