from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM CORSO C"""

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Corso(**row))

        cnx.close()
        cursor.close()
        return res

    @staticmethod
    def getStudentiByCorso(corso):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola = studente.matricola AND iscrizione.codins=%s
                        """

        cursor.execute(query,(corso,))
        res = []
        for row in cursor:
            res.append(Studente(**row))

        cnx.close()
        cursor.close()
        return res

    def getStudenteByMatricola(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT S.Nome, S.cognome 
                    FROM STUDENTE S
                    WHERE S.matricola = %s
                        """

        cursor.execute(query,(matricola,))
        print(cursor)
        res = []
        nome = ""
        cognome = ""
        for row in cursor:
            nome = row['Nome']
            cognome = row['cognome']

        cnx.close()
        cursor.close()
        return nome,cognome

    @staticmethod
    def getCorsiByMatricola(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT C.* 
                    FROM CORSO C, ISCRIZIONE I
                    WHERE I.codins=C.codins AND I.matricola = %s
                """

        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(**row))

        cnx.close()
        cursor.close()
        return res


if __name__ == "__main__":
    res = DAO.getStudenteByMatricola(190635)
    print (res)

