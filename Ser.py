import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(("127.0.0.1", 9000))
ser.listen(1)
print("SERVIDOR DE PRUEBA")
cli, addr = ser.accept()
if cli > 0:
	print ("CLIENTE CONECTADO")
while True:

    recibido = cli.recv(1024)
    #Mensaje Cliente Conectado 
    print "Cliente: " + str(addr[0]) + " Puerto: " + str(addr[1])
    #Devolvemos el mensaje al cliente
    cli.send("HOLA SOY EL SERVIDOR")

#Cerrar cliente y servidor
cli.close()
print("CLIENTE DESCONECTADO")
ser.close()
print ("CONEXIONES CERRADAS")
