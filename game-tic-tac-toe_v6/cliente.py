import socket
import time

class Cliente():
    """
    Class responsible for connecting the client to the server.

    ... 
    
    Methods
    -------
    enviar()
        Method responsible for sending message from the client to the server.

    """
    def __init__(self) -> None:
        self.ip = 'localhost'
        # self.ip = '10.180.45.118'
        self.port = 6969
        self.address = ((self.ip, self.port))
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(self.address)

    def enviar(self,mensagem : str):
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
        self.cliente_socket.send(mensagem.encode())
        recebeu = self.cliente_socket.recv(1024).decode()
        verificador = recebeu.split(",")
        if verificador[0] == "-1":  # sair
            self.cliente_socket.close()
        return verificador
