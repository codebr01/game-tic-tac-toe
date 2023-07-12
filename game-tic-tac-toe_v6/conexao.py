import mysql.connector as mysql

class Conexao:
    def __init__(self) -> None:
        self.conexao = mysql.connect(host = 'localhost',db = 'JogoDaVelha' ,user = 'root', passwd = 'meraldo20')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS player(
                      id INT AUTO_INCREMENT PRIMARY KEY, 
                      usuario VARCHAR(100) UNIQUE NOT NULL, 
                      nickname VARCHAR(100) UNIQUE NOT NULL,
                      email VARCHAR(200) UNIQUE NOT NULL, 
                      senha VARCHAR(20) NOT NULL);""")
    
    def cadastrar(self,lista):# [usuario,nickname,email,senha]

        existe = self.busca(lista[0])
        if existe == False:
            self.cursor.execute('INSERT INTO player(usuario,nickname,email,senha) VALUES(%s,%s,%s,%s)',(lista[0],lista[1],lista[2],lista[3]))
            self.conexao.commit()
            return True
        else:
            return False
        
    def busca(self,usuario):
        sql = """SELECT * FROM player WHERE usuario = (%s)"""
        val = usuario
        self.cursor.execute(sql,(val,))
        existe = self.cursor.fetchone()
        if existe != None:
            return existe
        else:
            return False

    
    def deletar(self,usuario):
        self.cursor.execute("DELETE FROM player WHERE usuario = (%s)",(usuario,))
        self.conexao.commit()

    def sairExe(self):
        self.conexao.commit()
        self.conexao.close()