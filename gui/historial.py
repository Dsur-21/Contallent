import customtkinter as ctk


class HistorialFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Historial",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=40)