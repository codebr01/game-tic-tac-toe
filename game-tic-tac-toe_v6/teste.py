# usuario = "joaoneto1417"
# senha = "joaoneto123"
# msg = "0"+"," + usuario + "," + senha
# msg1 = msg.split(",")
# print(msg,msg1)

# user = ("teste","senha","user")

# print("1" + ","+",".join(user))

# msg = "-1,"
# msg1 = msg.split(",")
# print(msg1)

# def tratar_mensagem(mensagem):
#     l = mensagem.split(",")
#     if l[0] == '-1':
#         envia = "-1"
#     return envia

# msg = "-1"
# print(tratar_mensagem(msg))

# lista = ['1','teste']
# lista.remove('1')
# print(lista)


# print("1\n")

# def teste():
#   tupla = (7, 'joaoneto1417', 'code3brxdxd', 'joaoneto@gmail.com', 'joaoneto123')
#   return "1," + str(tupla[0]) + "," + str(tupla[2])


# print(teste())

# import socket

# host = 'localhost'
# port = 7687
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((host, port))

# help(server_socket.sendto)

# def funcao_verifica(tabuleiro):
#     # Verificar linhas
#     for linha in tabuleiro:
#         if linha.count('X') == 3:
#             return 'X'
#         elif linha.count('O') == 3:
#             return 'O'

#     # Verificar colunas
#     for coluna in range(3):
#         if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'X':
#             return 'X'
#         elif tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'O':
#             return 'O'

#     # Verificar diagonais
#     if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
#         return 'X'
#     elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O' or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
#         return 'O'

#     # Nenhum vencedor encontrado
#     return None


# l = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']]

# print(l,funcao_verifica(l))

a = ''
b = None

if a == None:
    print("sim")
