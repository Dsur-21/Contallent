import customtkinter as ctk


class DocumentViewer(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Documento",
            font=("Arial", 22, "bold")
        )
        titulo.grid(row=0, column=0, pady=(20, 10))

        self.documento = ctk.CTkLabel(
            self,
            text="Aquí aparecerá el documento",
            fg_color="#ECECEC",
            corner_radius=10
        )
        self.documento.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.nombre = ctk.CTkLabel(
            self,
            text="Sin documento"
        )
        self.nombre.grid(
            row=2,
            column=0,
            pady=15
        )