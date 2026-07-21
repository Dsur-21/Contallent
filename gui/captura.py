import customtkinter as ctk


class CapturaFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Nueva práctica",
            font=("Arial", 28, "bold")
        )

        titulo.pack(pady=40)

        ctk.CTkLabel(
            self,
            text="Aquí aparecerá el documento que tendrás que capturar."
        ).pack()