import socket
import time
import threading
from conexao import Conexao

salas = []
users_online = []


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket, sinc):
        self.clientsocket = clientsocket
        self.clientAddress = clientAddress
        self.id = ''
        self.usuario = ''
        self.sinc = sinc
        super().__init__()

    def run(self):
        while True:
            recebe = self.clientsocket.recv(1024)
            enviar = tratar_mensagem(recebe.decode(),self.clientAddress)
            print("ENVIANDO: ", enviar)
            if enviar == "-1,":
                time.sleep(1)
                self.clientsocket.send(enviar.encode())
                break
            else:
                time.sleep(1)
                self.clientsocket.send(enviar.encode())


class Sala():
    def __init__(self,player1) -> None:
        self.qtd_players = []
        self.qtd_players.append(player1)
        self.jogou = ''
        self.jogadas = 0
        self.tabuleiro = ''
        self.vencedor = ''
        print("- =" * 15)
        print(f"PLAYERS: {self.qtd_players:} | NUMERO DE JOGADAS: {self.jogadas:}")
        print("- =" * 15)
    
    def addPlayer2(self,player2):
        self.qtd_players.append(player2)

    def verificarJogada(self,tabuleiro,player):
        if self.vencedor != None or self.jogadas > 9:
            self.tabuleiro = tabuleiro
            self.jogadas += 1
            self.jogou = 1
            print(f"JOGADA DO PLAYER: {player:} | NUMERO DE JOGADAS: {self.jogadas:}")
            if player == self.qtd_players[0]:
                if self.funcao_verifica(self.tabuleiro) == 'X':
                    self.vencedor = 'X'
                    return "1,"
                elif self.funcao_verifica(self.tabuleiro) == None:
                    return "2" + "," + str(self.tabuleiro[0][0]) + "," + str(self.tabuleiro[0][1]) + "," + str(self.tabuleiro[0][2]) + "," + str(self.tabuleiro[1][0]) + "," + str(self.tabuleiro[1][1]) + "," + str(self.tabuleiro[1][2]) + "," + str(self.tabuleiro[2][0]) + "," + str(self.tabuleiro[2][1]) + "," + str(self.tabuleiro[2][2])
            elif player == self.qtd_players[1]:
                if self.funcao_verifica(self.tabuleiro) == 'O':
                    self.vencedor = 'O'
                    return "1,"
                elif self.funcao_verifica(self.tabuleiro) == None:
                    return "2" + "," + str(self.tabuleiro[0][0]) + "," + str(self.tabuleiro[0][1]) + "," + str(self.tabuleiro[0][2]) + "," + str(self.tabuleiro[1][0]) + "," + str(self.tabuleiro[1][1]) + "," + str(self.tabuleiro[1][2]) + "," + str(self.tabuleiro[2][0]) + "," + str(self.tabuleiro[2][1]) + "," + str(self.tabuleiro[2][2])
            elif int(self.jogadas) > 9:
                print("entrou")
                self.vencedor = None
                print("68")
                return "3,"
        else:
            print("70")
            return "3,"

    
    def funcao_verifica(self,tabuleiro):
        # Verificar linhas
        for linha in tabuleiro:
            if linha.count('X') == 3:
                return 'X'
            elif linha.count('O') == 3:
                return 'O'

        # Verificar colunas
        for coluna in range(3):
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'X':
                return 'X'
            elif tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'O':
                return 'O'

        # Verificar diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
            return 'X'
        elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
            return 'O'

        # Nenhum vencedor encontrado
        return None
    
        


def tratar_mensagem(mensagem,address):
    l = mensagem.split(",")
    print(l)
    if l[0] == '-1':  # ['-1',''] - sair
        users_online.remove(address)
        print(f"USER DESCONNECTED: {newThread.clientAddress}")
        print(users_online)
        return "-1,"
    elif l[0] == '0':  # [0,usuario,senha] - login
        # (7, 'joaoneto1417', 'code3brxdxd', 'joaoneto@gmail.com', 'joaoneto123')
        user = conexao.busca(l[1])
        if user != False and user[4] == l[2]:
            newThread.id = user[0]
            newThread.usuario = user[1]
            print("- =" * 15) 
            print(f"Usuario conectado:{user:}\nPORTA THREAD: {newThread.clientAddress[1]:}")
            print("- =" * 15)
            # "1,7,code3brxdxd"
            return "1," + str(user[0]) + "," + str(user[2])
        else:
            return "0,"
    elif l[0] == '1':  # [1,usuario,nickname,email,senha] - cadastro
        l.remove('1')
        user = conexao.cadastrar(l)  # [usuario,nickname,email,senha]
        if user == True:
            return "1,"
        else:
            return "0,"
    elif l[0] == '2':
        if l[2] == '0':
            sala = Sala(address)
            salas.append(sala)
            return "1,"
        else:
            for sala in salas:
                if address in sala.qtd_players:
                    if len(sala.qtd_players) > 1:
                        return "1,"
                    else:
                        return "0,"
                else:
                    return "0,"
    elif l[0] == '3':
        for sala in salas:
            if len(sala.qtd_players) == 1:
                sala.addPlayer2(address)
                return "1,"
        return "0,"
    elif l[0] == '4':
        for sala in salas:
            if address in sala.qtd_players:
                if sala.vencedor != None:
                    msg = sala.verificarJogada([[l[1],l[2],l[3]],[l[4],l[5],l[6]],[l[7],l[8],l[9]]],address)
                    return msg
                else:
                    print("155")
                    return "3,"


    elif l[0] == '5':
        for sala in salas:
            if address in sala.qtd_players:
                if sala.vencedor == '':
                    if sala.jogadas < 9:
                        if sala.jogou == 1:
                            sala.jogou = 0
                            return "1" + "," + str(sala.tabuleiro[0][0]) + "," + str(sala.tabuleiro[0][1]) + "," + str(sala.tabuleiro[0][2]) + "," + str(sala.tabuleiro[1][0]) + "," + str(sala.tabuleiro[1][1]) + "," + str(sala.tabuleiro[1][2]) + "," + str(sala.tabuleiro[2][0]) + "," + str(sala.tabuleiro[2][1]) + "," + str(sala.tabuleiro[2][2])
                        else:
                            return "0,"
                    else:
                        print("169")
                        return "3,"
                else:
                    print("171")
                    return "3,"
        return "0,"


if __name__ == "__main__":
    host = 'localhost'
    port = 9876
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    conexao = Conexao()
    sinc = threading.Lock()

    while True:
        server_socket.listen(10)
        print("esperando cliente...")
        clientsock, clientAddress = server_socket.accept()
        print("cliente aceito...")
        newThread = ClientThread(clientAddress, clientsock,sinc)
        print(clientAddress)
        newThread.start()
        users_online.append(newThread.clientAddress)