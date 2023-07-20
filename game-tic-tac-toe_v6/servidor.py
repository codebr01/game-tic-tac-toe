import socket
import time
import threading
from conexao import Conexao
from random import randint

salas = []
users_online = []

class ClientThread(threading.Thread):
    """
    Class used to create a thread from a new connection.

    ... 

    Attributes
    ----------
    clientAddress : (IP : str, PORT : int)
        This attribute has the purpose of generating the user's connection to the server.
    clientsocket : socket.socket
        This attribute has the purpose of creating an object of type socket.
    sinc : threading.Lock
        This attribute has the purpose of creating a lock on your thread in your user connection to the server.
    
    Methods
    -------
    run()
        Initializer method of the spawned thread.

    """
    def __init__(self, clientAddress : tuple, clientsocket : socket.socket, sinc : threading.Lock):
        """
        Parameters
        ----------
        clientAddress : tuple
            This attribute has the purpose of generating the user's connection to the server.
        clientsocket : socket.socket
            This attribute has the purpose of creating an object of type socket.
        sinc : threading.Lock
            This attribute has the purpose of creating a lock on your thread in your user connection to the server.
        """
        self.clientsocket = clientsocket
        self.clientAddress = clientAddress
        self.minha_sala = None
        self.sala_jogando = None
        self.sinc = sinc
        super().__init__()

    def run(self):
        """
        Initializer method of the spawned thread.

        This method will perform the iteration between the client and the server, making requests on the server and sending the response to the client. 
        """
        while True:
            recebe = self.clientsocket.recv(1024)
            # self.sinc.acquire()
            enviar = tratar_mensagem(recebe.decode())
            # self.sinc.release()
            print("SERVIDOR ENVIANDO: ", enviar)
            if enviar == "-1,":
                self.clientsocket.send(enviar.encode())
                break
            else:
                self.clientsocket.send(enviar.encode())


class Sala():
    """
    Class used to manage rooms for users to play.

    ...

    Attributes
    ----------
    player1 : tuple
        This attribute has the purpose of generating the user's connection to the server.
        
    Methods
    -------
    addPlayer2()
        Method used to add the second player in the room.
    verificarJogada()
        Method used to check the player's move.
    funcao_verifica()
        Auxiliary function that checks the board.

    """
    def __init__(self, player1_id : int) -> None:
        """
        Parameters
        ----------
        player1_id : int
            This attribute is the identifier of the user who requested a room from the server to play in.
        """
        self.player1 = player1_id
        self.player2 = None
        self.id_sala = randint(0,5000)
        self.jogou = ''
        self.jogadas = 0
        self.tabuleiro = ''
        self.vencedor = ''
        self.aberta = 0

    def addPlayer2(self, player2_id : int):
        """
        Method adds the second player to the room.

        This method will add the second player that searched for an open room.

        Parameters
        ----------
        player2 : int
            Identifier of the user who requested access to a room open to the server to play.
        """
        self.player2 = player2_id

    def verificarJogada(self, tabuleiro : list, player_id : int):
        """
        Method checks the playing of the player.

        ...

        Parameters
        ----------
        tabuleiro : list
            play performed by the user.
        player_id : int
            user who performed the move.

        Returns
        -------
        "1," : str
            Returns when the user won the match.
        "2," : str
            Returns when the user performed a move and did not win.
        "4," : str
            Returns when the user will perform the move and the previous move by player 2 won.
        
        """
        self.tabuleiro = tabuleiro
        self.jogadas += 1
        self.jogou = 1
        print("- =" * 25)
        print(f"JOGADA DO PLAYER: {player_id:} | NUMERO DE JOGADAS: {self.jogadas:}")
        print("- =" * 25)
        if player_id == self.player1:
            verificador = self.funcao_verifica(self.tabuleiro)
            print("VERIFICADOR PLAYER1: ", verificador)
            if verificador == 'X':
                self.aberta = 0
                self.vencedor = 'X'
                return "1,"
            elif verificador == None:
                return "2" + "," + str(self.tabuleiro[0][0]) + "," + str(self.tabuleiro[0][1]) + "," + str(self.tabuleiro[0][2]) + "," + str(self.tabuleiro[1][0]) + "," + str(self.tabuleiro[1][1]) + "," + str(self.tabuleiro[1][2]) + "," + str(self.tabuleiro[2][0]) + "," + str(self.tabuleiro[2][1]) + "," + str(self.tabuleiro[2][2])
        elif player_id == self.player2:
            verificador = self.funcao_verifica(self.tabuleiro)
            print("VERIFICADOR PLAYER2: ", verificador)
            if verificador == 'O':
                self.aberta = 0
                self.vencedor = 'O'
                return "1,"
            elif verificador == None:
                return "2" + "," + str(self.tabuleiro[0][0]) + "," + str(self.tabuleiro[0][1]) + "," + str(self.tabuleiro[0][2]) + "," + str(self.tabuleiro[1][0]) + "," + str(self.tabuleiro[1][1]) + "," + str(self.tabuleiro[1][2]) + "," + str(self.tabuleiro[2][0]) + "," + str(self.tabuleiro[2][1]) + "," + str(self.tabuleiro[2][2])
        elif int(self.jogadas) > 9:
            self.aberta = 0
            self.vencedor = None
            return "4,"

    def funcao_verifica(self, tabuleiro : list):
        """
        Method checks the list passed by the current user.

        ...

        Parameters
        ----------
        tabuleiro : list
            Player movement.

        Returns
        -------
        'X' : str
            Returns when player 1 wins.
        'O' : str
            Returns when player 2 wins.
        None : NoneType
            Returns when the current player does not win.
        """
        for linha in tabuleiro:
            if linha.count('X') == 3:
                return 'X'
            elif linha.count('O') == 3:
                return 'O'

        for coluna in range(3):
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'X':
                return 'X'
            elif tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'O':
                return 'O'

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
            return 'X'
        elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
            return 'O'

        return None

def tratar_mensagem(mensagem : str):
    """
    Method will handle the message received from the client.

    This method deals with the message received from the client, where it transforms the message into a list and the first position in the list is the operation requested from the server. Where within the options provided there are login, registration, logout, create a room, enter an open room, ask if you can play and play.
    Parameters
    ----------
    mensagem : str
        Client mensagem.

    Returns
    -------
    "-1," : str
        Returns when the user disconnects from the server.
    
    """
    print("CLIENTE-THREAD: ",newThread.clientAddress,"ENVIOU: ", mensagem)
    l = mensagem.split(",")
    print(l)
    if l[0] == '-1':
        print(f"USER DESCONNECTED: {newThread.clientAddress} - ID: {l[1]:}")
        # users_online.remove(l[1])
        return "-1,"
    elif l[0] == '0':
        user = conexao.busca(l[1])
        if user != False and user[4] == l[2]:
            print("- =" * 15)
            print(f"Usuario conectado:{user[1]:} - ID USER_BD: {user[0]:} - PORTA THREAD: {newThread.clientAddress:}")
            print("- =" * 15)
            users_online.append(user[0])
            return "1," + str(user[0]) + "," + str(user[2]) 
        else:
            return "0,"
    elif l[0] == '1':
        l.remove('1')
        user = conexao.cadastrar(l)
        if user == True:
            return "1,"
        else:
            return "0,"
    elif l[0] == '2':
        if l[2] == '0':
            sala = Sala(l[1])
            newThread.minha_sala = sala
            newThread.minha_sala.aberta = 1
            print(f"SALA CRIADA - ID SALA: {newThread.minha_sala.id_sala:} - PLAYER1 : {newThread.minha_sala.player1:} - PLAYER2 : {newThread.minha_sala.player2:}")
            salas.append(sala)
            return "1," + str(newThread.minha_sala.id_sala) + ","
        else:
            if newThread.minha_sala.player2 != None:
                print(f"ENTRANDO NA SALA - ID SALA: {newThread.minha_sala.id_sala:} - PLAYER1 : {newThread.minha_sala.player1:} - PLAYER2 : {newThread.minha_sala.player2:}")
                return "1,"
            else:
                return "0,"
    elif l[0] == '3':
        for sala in salas:
            print(f"PLAYER {l[1]:} TENTANDO NA SALA {sala.id_sala:} - STATUS SALA: {sala.aberta:}")
            if sala.aberta == 1:
                sala.aberta = 0
                newThread.sala_jogando = sala
                sala.addPlayer2(l[1])
                print("ENTRANDO NA SALA: ", sala.id_sala, "PLAYER1: ",sala.player1,"PLAYER2: ",sala.player2)
                return "1," + str(sala.id_sala) + ","
        return "0," 
    elif l[0] == '4':
        if l[10] == newThread.minha_sala.player1:
            newThread.minha_sala.jogou = 0
            msg = newThread.minha_sala.verificarJogada([[l[1], l[2], l[3]], [l[4], l[5], l[6]], [l[7], l[8], l[9]]], l[10])
            return msg
        else:
            newThread.sala_jogando.jogou = 0
            msg = newThread.sala_jogando.verificarJogada([[l[1], l[2], l[3]], [l[4], l[5], l[6]], [l[7], l[8], l[9]]], l[10])
            return msg
    elif l[0] == '5':
        if newThread.minha_sala.player1 == l[1]:
            if newThread.minha_sala.vencedor == 'X':
                print("FECHANDO SALA PLAYER1 GANHOU")
                newThread.minha_sala.aberta = 0
                return "5,"
            if newThread.minha_sala.vencedor == 'O':
                newThread.minha_sala.aberta = 0
                print("FECHANDO SALA PLAYER1 PERDEU")
                return "3,"
            if newThread.minha_sala.vencedor == None or newThread.minha_sala.jogadas == 9:
                newThread.minha_sala.aberta = 0
                print("FECHANDO SALA PLAYER1 EMPATE")
                return "4,"
            if newThread.minha_sala.jogadas < 9 and newThread.minha_sala.jogou == 1:
                newThread.minha_sala.jogou = 0
                return "1" + "," + str(newThread.minha_sala.tabuleiro[0][0]) + "," + str(newThread.minha_sala.tabuleiro[0][1]) + "," + str(newThread.minha_sala.tabuleiro[0][2]) + "," + str(newThread.minha_sala.tabuleiro[1][0]) + "," + str(newThread.minha_sala.tabuleiro[1][1]) + "," + str(newThread.minha_sala.tabuleiro[1][2]) + "," + str(newThread.minha_sala.tabuleiro[2][0]) + "," + str(newThread.minha_sala.tabuleiro[2][1]) + "," + str(newThread.minha_sala.tabuleiro[2][2])
            else:
                return "0,"
        else:
            if newThread.sala_jogando.vencedor == 'O':
                print("FECHANDO SALA PLAYER2 GANHOU")
                newThread.sala_jogando.aberta = 0
                return "5,"
            if newThread.sala_jogando.vencedor == 'X':
                print("FECHANDO SALA PLAYER2 PERDEU")
                newThread.sala_jogando.aberta = 0
                return "3,"
            if newThread.sala_jogando.vencedor == None or newThread.sala_jogando.jogadas == 9:
                print("FECHANDO SALA PLAYER2 EMPATE")
                newThread.sala_jogando.aberta = 0
                return "4,"
            if newThread.sala_jogando.jogadas < 9 and newThread.sala_jogando.jogou == 1:
                newThread.minha_sala.jogou = 0
                return "1" + "," + str(newThread.sala_jogando.tabuleiro[0][0]) + "," + str(newThread.sala_jogando.tabuleiro[0][1]) + "," + str(newThread.sala_jogando.tabuleiro[0][2]) + "," + str(newThread.sala_jogando.tabuleiro[1][0]) + "," + str(newThread.sala_jogando.tabuleiro[1][1]) + "," + str(newThread.sala_jogando.tabuleiro[1][2]) + "," + str(newThread.sala_jogando.tabuleiro[2][0]) + "," + str(newThread.sala_jogando.tabuleiro[2][1]) + "," + str(newThread.sala_jogando.tabuleiro[2][2])
            else:
                return "0,"


if __name__ == "__main__":
    host = 'localhost'
    # host = '10.180.45.118'
    port = 6969
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    conexao = Conexao()
    sinc = threading.Lock()

    while True:
        server_socket.listen(10)
        print("esperando cliente...")
        clientsock, clientAddress = server_socket.accept()
        print("cliente aceito...")
        newThread = ClientThread(clientAddress, clientsock, sinc)
        print(clientAddress)
        newThread.start()
