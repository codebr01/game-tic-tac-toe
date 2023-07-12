import socket
ip = 'localhost'
port = 9876
address = ((ip,port))
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(address)

def enviar(mensagem):
    cliente_socket.send(mensagem.encode())
    recebeu = cliente_socket.recv(1024).decode()
    verificador = recebeu.split(",")
    if verificador[0] == "-1":#sair
        cliente_socket.close()
    return verificador
