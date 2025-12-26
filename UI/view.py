import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorsi = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)


        self.ddCorsi = ft.Dropdown(label="Corso", width= 500)
        self._controller.popolaDDCorso()
        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click = self._controller.handleCercaIscritti)
        row1 = ft.Row([self.ddCorsi, self.btnCercaIscritti])

        self.txtMatricola = ft.TextField(label="Matricola", width= 100)
        self.txtCognomeStudente = ft.TextField(label="Cognome Studente", disabled=True)
        self.txtNomeStudente = ft.TextField(label="Nome Studente", disabled=True)
        row2 = ft.Row([self.txtMatricola, self.txtNomeStudente, self.txtCognomeStudente])

        self.btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click = self._controller.handleCercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click = self._controller.handleCercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click = self._controller.handleIscrivi)
        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi], alignment=MainAxisAlignment.CENTER)

        self.lvOut = ft.ListView(expand=True)

        self._page.add(row1,row2,row3,self.lvOut)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
