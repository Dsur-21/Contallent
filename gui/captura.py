import customtkinter as ctk

from gui.components.document_viewer import DocumentViewer
from gui.components.capture_form import CaptureForm
from services.document_manager import DocumentManager


class CapturaFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.viewer = DocumentViewer(self)
        self.viewer.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

        manager = DocumentManager()
        documento = manager.get_random_document()
        if documento:
            self.viewer.load_document(documento)

        self.formulario = CaptureForm(self)
        self.formulario.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)