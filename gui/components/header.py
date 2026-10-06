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

        self.usuario_label = ctk.CTkLabel(
            self,
            text="Usuario: "
        )

        self.usuario_label.pack(
            side="right",
            padx=20
        )

    def set_user(self, usuario):

        self.usuario_label.configure(
            text=f"Usuario: {usuario}"
        )