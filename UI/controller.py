import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def popolaDDCorso(self):
        for c in self._model.getAllCorsi():
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=c.codins, text=c))
            #self._view.ddCorsi.options.append(ft.dropdown.Option(key=str(c.codins)))
            self._view.update_page()

    def choiseDD(self, e):
        self.choiseDDTipoCorso = e.control.data
        print(type(self.choiseDDTipoCorso))

    def handleCercaIscritti(self,e):
        print(self._view.ddCorsi.value)
        if self._view.ddCorsi.value is None:
            self._view.lvOut.controls.append(ft.Text("Attenzione, selezionare un corso"))
            self._view.update_page()
            return
        self._view.lvOut.controls.clear()
        studenti = self._model.getStudentiByCorso(self._view.ddCorsi.value)
        print(len(studenti))
        self._view.lvOut.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso:"))
        for s in studenti:
            self._view.lvOut.controls.append(ft.Text(s))

        self._view.update_page()

    def handleCercaStudente(self,e):
        print(self._view.txtMatricola)
        self._view.lvOut.controls.clear()
        (nome, cognome) = self._model.getStudenteByMatricola(self._view.txtMatricola.value)
        print(nome,cognome)
        if (nome,cognome) == ("",""):
            self._view.lvOut.controls.append(ft.Text("Studente non presente nel database"))
            self._view.update_page()
            return

        self._view.lvOut.controls.clear()
        self._view.txtNomeStudente.value = nome
        self._view.txtCognomeStudente.value = cognome

        self._view.update_page()

    def handleCercaCorsi(self,e):
        matricola = self._view.txtMatricola.value
        self._view.lvOut.controls.clear()
        corsi = self._model.getCorsiByMatricola(matricola)
        if len(corsi) == 0:
            self._view.lvOut.controls.append(ft.Text("Studente non presente nel database"))
            self._view.update_page()
            return

        self._view.lvOut.controls.clear()
        for c in corsi:
            self._view.lvOut.controls.append(ft.Text(f"{c} \n"))

        self._view.update_page()


    def handleIscrivi(self,e):
        pass
