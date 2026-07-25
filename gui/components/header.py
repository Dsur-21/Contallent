import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=60)

        self.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self,
            text="Simulador de Captura Documental",
            font=("Arial", 20, "bold")
        )

        titulo.pack(side="left", padx=20)

        usuario = ctk.CTkLabel(
            self,
            text="Usuario: lpz$med"
        )

        usuario.pack(side="right", padx=20)