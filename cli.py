import socket

host = '127.0.0.1'
port = 9000

obj = socket.socket()
obj.connect((host, port))
print("CLIENTE")
print("Conectado al servidor")
 
while True:
    mens = raw_input("Mensaje para ti bienvenido >> ")
    obj.send(mens)
obj.close()
#Cuando las conecciones cierran
print("Conexion cerrada")

