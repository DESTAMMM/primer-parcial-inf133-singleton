from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Player:
    _instance = None

    def __new__(cls, id, nombre, number, status):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.id= id
            cls._instance.nombre = nombre
            cls._instance.number = number
            cls._instance.attempts = []
            cls._instance.status = status
        return cls._instance
    
    def to_dict(self):
        return {"nombre": self.nombre, "attemps": self.attemps "status": self.status}
        
class PlayerServices:
    guess=[]

    def add_game(data):
        id = guess.len()+1
        nombre=data.nombre()
        number=random.randint(1,100)
        status="En progreso"
        player=Player.__new__(id,nombre,number,status)
        if guess==null:
            guess.append(player)
        else:
            guess[1]=player
        
    def list_game():
        return guess

    def update_game(id, attemp):
        for player in guess if player[id]==id:
            player.attemps.append[attemp]
            if attemp == player.number:
                return "message: ¡Felicitaciones! Has adivinado el numero"
            elif attemp >= player.number:
                return "message: El numero a adivinar es menor"
            elif attemp <= player.number:
                return "message: El numero a adivinar es mayor"

    def delete_game(id):
        for player in guess if player[id]==id:
            guess.pop(id)
        return player

    def filtrar_por_id(id):
        for player in guess if player[id]==id:
            return player
        
    def filtrar_por_nombre(nombre):
        for player in guess if player[nombre]==nombre:

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
    
    def do_PUT(self):
    
    def do_DELETE(self):
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
