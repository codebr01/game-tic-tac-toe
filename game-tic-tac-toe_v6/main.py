import sys
import os
import typing
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget
from PyQt5.QtCore import QCoreApplication

from telas.tela_cadastro import Tela_Cadastro
from telas.tela_inicial import Tela_Inicial
from telas.tela_login import Tela_Login
from telas.tela_principal import Tela_Principal
from telas.tela_jogar_offline import Tela_Jogar_Offline
from telas.tela_jogar_online import Tela_Jogar_Online
from telas.tela_jogar_online_tabuleiro import Tela_Jogar_Online_Tabuleiro
from telas.tela_jogar_online_tabuleiro_sem_botao import Tela_Jogar_Online_Tabuleiro_Sem_Botao


import cliente
dados = []

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(800,600)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        
        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack2)
        
        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack3)

        self.tela_jogar_offline = Tela_Jogar_Offline()
        self.tela_jogar_offline.setupUi(self.stack4)

        self.tela_jogar_online = Tela_Jogar_Online()
        self.tela_jogar_online.setupUi(self.stack5)

        self.tela_jogar_online_tabuleiro = Tela_Jogar_Online_Tabuleiro()
        self.tela_jogar_online_tabuleiro.setupUi(self.stack6)

        self.tela_jogar_online_tabuleiro_sem_botao = Tela_Jogar_Online_Tabuleiro_Sem_Botao()
        self.tela_jogar_online_tabuleiro_sem_botao.setupUi(self.stack7)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

class Main(QMainWindow,Ui_Main):
    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.tela_inicial.botarSair.clicked.connect(self.sairExe)
        self.tela_inicial.botaoCadastrar.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.botaoLogar.clicked.connect(self.abrirTelaLogin)

        self.tela_cadastro.botaoVoltar.clicked.connect(self.voltarTelaInicial)
        self.tela_cadastro.botaoCadastrar.clicked.connect(self.cadastrarPlayer)

        self.tela_login.botaoVoltar.clicked.connect(self.voltarTelaInicial)
        self.tela_login.botarEntrar.clicked.connect(self.tentarLogin)
        
        self.tela_principal.botarSair.clicked.connect(self.sairExe)
        self.tela_principal.botarDesconectar.clicked.connect(self.abrirTelaLoginDesconectar)
        self.tela_principal.botaoJogarOffline.clicked.connect(self.abrirTelaJogarOfflineSetVoid)
        self.tela_principal.botaoJogarOnline.clicked.connect(self.JogarOnline)

        self.tela_jogar_offline.botaoJogar.clicked.connect(self.resultadoFinal)
        self.tela_jogar_offline.botaoVoltar.clicked.connect(self.abrirTelaPrincipal)

        self.tela_jogar_online.botaoVoltar.clicked.connect(self.abrirTelaPrincipal)
        self.tela_jogar_online.entrarFila.clicked.connect(self.entrarFila)
        self.tela_jogar_online.procurarPartid.clicked.connect(self.procurarPartida)

        self.tela_jogar_online_tabuleiro.botaoJogar.clicked.connect(self.botaoJogarOnlineTabuleiro)



    def voltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaPrincipal(self):
        self.QtStack.setCurrentIndex(3)
        self.tela_principal.label_6.setText(dados[1])

    def JogarOnline(self):
        self.QtStack.setCurrentIndex(5)

    
    def abrirTelaLoginDesconectar(self):
        QMessageBox.information(None,'ERROR','FUNÇÃO NÃO ESTA PRONTA')

    def abrirTelaJogarOnlineTabuleiro(self):
        self.QtStack.setCurrentIndex(6)

    def abrirTelaJogarOnlineTabuleiroSemBotao(self):
        self.QtStack.setCurrentIndex(7)    
        time.sleep(1)
        msg = "5,"
        recebeu = cliente.enviar(msg)
        if recebeu[0] == '0':
            self.abrirTelaJogarOnlineTabuleiroSemBotao()
        elif recebeu[0] == '1':
            self.tela_jogar_online_tabuleiro.lineEdit.setText(recebeu[1])
            self.tela_jogar_online_tabuleiro.lineEdit_2.setText(recebeu[2])
            self.tela_jogar_online_tabuleiro.lineEdit_3.setText(recebeu[3])
            self.tela_jogar_online_tabuleiro.lineEdit_4.setText(recebeu[4])
            self.tela_jogar_online_tabuleiro.lineEdit_5.setText(recebeu[5])
            self.tela_jogar_online_tabuleiro.lineEdit_6.setText(recebeu[6])
            self.tela_jogar_online_tabuleiro.lineEdit_7.setText(recebeu[7])
            self.tela_jogar_online_tabuleiro.lineEdit_8.setText(recebeu[8])
            self.tela_jogar_online_tabuleiro.lineEdit_9.setText(recebeu[9])
            self.abrirTelaJogarOnlineTabuleiro()
        elif recebeu[0] == '3':
            self.abrirTelaPrincipal()
            QMessageBox.information(None,'PARTIDA','RODADA FINALIZADA')

    def botaoJogarOnlineTabuleiro(self):
        l = [[self.tela_jogar_online_tabuleiro.lineEdit.text(),self.tela_jogar_online_tabuleiro.lineEdit_2.text(),self.tela_jogar_online_tabuleiro.lineEdit_3.text()],[self.tela_jogar_online_tabuleiro.lineEdit_4.text(),self.tela_jogar_online_tabuleiro.lineEdit_5.text(),self.tela_jogar_online_tabuleiro.lineEdit_6.text()],[self.tela_jogar_online_tabuleiro.lineEdit_7.text(),self.tela_jogar_online_tabuleiro.lineEdit_8.text(),self.tela_jogar_online_tabuleiro.lineEdit_9.text()]]
        msg = "4" + "," + str(l[0][0]) + "," + str(l[0][1]) + "," + str(l[0][2]) + "," + str(l[1][0]) + "," + str(l[1][1]) + "," + str(l[1][2]) + "," + str(l[2][0]) + "," + str(l[2][1]) + "," + str(l[2][2])
        recebeu = cliente.enviar(msg)
        if recebeu[0] == '2':
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit.setText(recebeu[1])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_2.setText(recebeu[2])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_3.setText(recebeu[3])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_4.setText(recebeu[4])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_5.setText(recebeu[5])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_6.setText(recebeu[6])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_7.setText(recebeu[7])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_8.setText(recebeu[8])
            self.tela_jogar_online_tabuleiro_sem_botao.lineEdit_9.setText(recebeu[9])
            self.abrirTelaJogarOnlineTabuleiroSemBotao()
        elif recebeu[0] == '3':
            self.abrirTelaPrincipal()
            QMessageBox.information(None,'PARTIDA','NGM VENCEU')
        else:
            self.abrirTelaPrincipal()
            QMessageBox.information(None,'SUCESSO','PARABENS VOCE VENCEU')


    def cadastrarPlayer(self):
        usuario = self.tela_cadastro.lineEdit_4.text()
        nickname = self.tela_cadastro.lineEdit_5.text()
        email = self.tela_cadastro.lineEdit_6.text()
        senha = self.tela_cadastro.lineEdit_7.text()
        if usuario != '' and nickname != '' and email != '' and senha != '':
            msg = "1"+ "," + usuario + "," + nickname + "," + email + "," + senha
            recebeu = cliente.enviar(msg)
            if recebeu == '1':
                self.tela_cadastro.lineEdit_4.setText('')
                self.tela_cadastro.lineEdit_5.setText('')
                self.tela_cadastro.lineEdit_6.setText('')
                self.tela_cadastro.lineEdit_7.setText('')
                QMessageBox.information(None,'SUCESSO','Usuario cadastrado')
            else:
                QMessageBox.information(None,'FALHA','Usuario já cadastrado')
        else:
            QMessageBox.information(None,'FALHA','Todos os campos devem ser preenchidos')

    def tentarLogin(self):
        usuario = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if usuario != '' and senha != '':
            msg = "0"+ "," + usuario + "," + senha
            recebeu = cliente.enviar(msg)#"0,usuario,senha"
            recebeu.append('0')
            if recebeu[0] != '0':#[1,7,code3brxdxd,0]
                dados.append(recebeu[1])
                dados.append(recebeu[2])
                dados.append(recebeu[3])
                self.abrirTelaPrincipal()
            else:
                QMessageBox.information(None,'FALHA','Senha Incorreta ou Usuario Incorreto')
        else:
            QMessageBox.information(None,'FALHA','Todos os campos devem ser preenchidos')
        


    def setarTabuleiro(self):
        self.tela_jogar_offline.lineEdit.setText(' ')
        self.tela_jogar_offline.lineEdit_2.setText(' ')
        self.tela_jogar_offline.lineEdit_3.setText(' ')
        self.tela_jogar_offline.lineEdit_4.setText(' ')
        self.tela_jogar_offline.lineEdit_5.setText(' ')
        self.tela_jogar_offline.lineEdit_6.setText(' ')
        self.tela_jogar_offline.lineEdit_7.setText(' ')
        self.tela_jogar_offline.lineEdit_8.setText(' ')
        self.tela_jogar_offline.lineEdit_9.setText(' ')

    def abrirTelaJogarOfflineSetVoid(self):
        self.setarTabuleiro()
        self.abrirTelaJogarOffline()

    def abrirTelaJogarOffline(self):
        self.QtStack.setCurrentIndex(4)

    def resultadoFinal(self):
        resultado = self.verificar_vitoria()
        if resultado != None:
            QMessageBox.information(None,'RESULTADO',f'Vencedor: {resultado:}')
        else:
            QMessageBox.information(None,'RESULTADO','Não Há Vencedor')
        self.setarTabuleiro()
    
    def entrarFila(self):
        if dados[2] == '0':
            msg = "2," + str(dados[0]) + "," + str(dados[2])
            recebeu = cliente.enviar(msg)
            if recebeu[0] == '1':
                dados[2] = '1'
                while True:
                    time.sleep(2)
                    msg = "2," + str(dados[0]) + "," + str(dados[2])
                    recebeu = cliente.enviar(msg)
                    if recebeu[0] == '0':
                        continue
                    else:
                        break
                dados[2] = '0'
                self.abrirTelaJogarOnlineTabuleiro()
            else:
                QMessageBox.information(None,'LARAPIO','VOCE JA ESTÁ NA FILA, NEM PENSAR RAPAZ')
        else:
            QMessageBox.information(None,'LARAPIO','VOCE JA ESTÁ NA FILA, NEM PENSAR RAPAZ')

    def procurarPartida(self):
        msg = "3," + str(dados[0])
        time.sleep(1)
        recebeu = cliente.enviar(msg)
        if recebeu[0] != '0':
            self.abrirTelaJogarOnlineTabuleiroSemBotao()
        else:
            QMessageBox.information(None,'ERRO','OPS e.e PARECE QUE A FILA ESTÁ VAZIA....')

    #colocar a função aqui
    
    def verificar_vitoria(self):
        tabuleiro = [[self.tela_jogar_offline.lineEdit.text(),self.tela_jogar_offline.lineEdit_2.text(),self.tela_jogar_offline.lineEdit_3.text()],[self.tela_jogar_offline.lineEdit_4.text(),self.tela_jogar_offline.lineEdit_5.text(),self.tela_jogar_offline.lineEdit_6.text()],[self.tela_jogar_offline.lineEdit_7.text(),self.tela_jogar_offline.lineEdit_8.text(),self.tela_jogar_offline.lineEdit_9.text()]]
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

    def sairExe(self):
        msg = "-1,"
        recebeu = cliente.enviar(msg)
        print(recebeu)
        exit()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())