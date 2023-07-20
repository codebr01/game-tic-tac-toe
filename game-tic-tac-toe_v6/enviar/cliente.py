import socket
import time
# ip = 'localhost'
ip = '10.180.45.118'
port = 6969
address = ((ip, port))
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(address)


def enviar(mensagem : str):
    """
    Method sends message to server.

    This method will send the user's message to the server.

    Parameters
    ----------
    mensagem : str
        User mensagem.

    Returns
    -------
    verificador : list
        Returns the message returned from the server in list form.
    
    """
    time.sleep(1)
    cliente_socket.send(mensagem.encode())
    recebeu = cliente_socket.recv(1024).decode()
    verificador = recebeu.split(",")
    if verificador[0] == "-1":  # sair
        cliente_socket.close()
    return verificador
