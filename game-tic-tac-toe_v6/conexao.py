import mysql.connector as mysql

class Conexao:
    """
    Class used to create database connection.

    This class is the server's connection to the database, which provides user data. 

    Attributes
    ----------
    ...
    
    Methods
    -------
    cadastrar()
        Register a user in the database.
    busca()
        Search a user in the database.
    deletar()
        Delete a user from the database.
    sairExe()
        Closes user access to the database.

    """
    def __init__(self) -> None:

        self.conexao = mysql.connect(host = 'localhost',db = 'JogoDaVelha' ,user = 'root', passwd = 'meraldo20')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS player(id INT AUTO_INCREMENT PRIMARY KEY, usuario VARCHAR(100) UNIQUE NOT NULL, nickname VARCHAR(100) UNIQUE NOT NULL, email VARCHAR(200) UNIQUE NOT NULL, senha VARCHAR(20) NOT NULL);""")
    
    def cadastrar(self,lista : list):
        """
        Register a user in the database.

        This method receives data from a user and tries to register.

        Parameters
        ----------
        lista : list
            Data received from the user.

        Returns
        -------
        True : bool
            Returns when the received data is not in the database and the user can be registered.
        False : bool
            Returns when the received data is in the database and the user cannot be registered.
        
        """
        existe = self.busca(lista[0], lista[2])
        if existe == False:
            self.cursor.execute('INSERT INTO player(usuario,nickname,email,senha) VALUES(%s,%s,%s,%s)',(lista[0],lista[1],lista[2],lista[3]))
            self.conexao.commit()
            return True
        else:
            return False
        
    def busca(self,usuario : str):
        """
        Search a user in the database.

        This method looks for a user in the database.

        Parameters
        ----------
        usuario : str
            User's primary login.

        Returns
        -------
        existe : tuple
            Returns when the specified user exists in the database.
        False : bool
            Returns when the specified user does not exist in the database.
        
        """
        sql = """SELECT * FROM player WHERE usuario = (%s)"""
        val = usuario
        self.cursor.execute(sql,(val,))
        existe = self.cursor.fetchone()
        if existe != None:
            return existe
        else:
            return False
    
    def deletar(self,usuario : str):
        """
        Delete a user from the database.

        ...

        Parameters
        ----------
        usuario : str
            User received to be deleted.
        
        """
        self.cursor.execute("DELETE FROM player WHERE usuario = (%s)",(usuario,))
        self.conexao.commit()

    def sairExe(self):
        """
        Closes the connection between the user connected to the server and the database.

        ...
        
        """
        self.conexao.commit()
        self.conexao.close()