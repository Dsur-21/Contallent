import customtkinter as ctk

from gui.components.document_viewer import DocumentViewer
from gui.components.capture_form import CaptureForm
from services.document_manager import DocumentManager
from services.practice_session import PracticeSession



class CapturaFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.practice_session = PracticeSession()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.btn_nueva_practica = ctk.CTkButton(
            self,
            text = "Nueva práctica",
            command = self.start_practice
        )

        self.btn_nueva_practica.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            pady = (0, 15)
        )

        self.viewer = DocumentViewer(self)
        self.viewer.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)


        self.formulario = CaptureForm(self)
        self.formulario.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

    def start_practice(self):

        self.practice_session.start()
        
        documento = self.practice_session.next_document()

        if documento:
            self.viewer.load_document(documento)
            self.formulario.clear()