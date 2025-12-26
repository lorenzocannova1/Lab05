from database.corso_DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getStudentiByCorso(self,corso):
        return DAO.getStudentiByCorso(corso)

    def getStudenteByMatricola(self,matricola):
        return DAO.getStudenteByMatricola(matricola)

    def getCorsiByMatricola(self,matricola):
        return DAO.getCorsiByMatricola(matricola)