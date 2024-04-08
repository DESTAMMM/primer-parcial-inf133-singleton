from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Player:
    _instance = None

    def __new__(cls, nombre, status):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.number = number
            cls._instance.attempts = []
            cls._instance.status = status
        return cls._instance
    
    def to_dict(self):
        return {"nombre": self.nombre, "attemps": self.attemps "status": self.status}
        
class PlayerServices:
    games=[]

    def add_game(data):
        
    def list_game():

    def update_game(data):

    def delete_game(id):

    def filtrar_por_id(id):
        
    def filtrar_por_nombre(nombre):

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        data = handler.rfile.read(content_length)
        return json.loads(data.decode("utf-8"))
        
class PlayerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        

    def do_POST(self):
        

def main():
    global player
    player = Player("Julian")

    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, PlayerHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()
