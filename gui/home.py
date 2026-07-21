import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Bienvenido",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=(40, 10))

        descripcion = ctk.CTkLabel(
            self,
            text="Simulador profesional de captura documental.",
            font=("Arial", 18)
        )
        descripcion.pack(pady=(0, 30))

        nueva = ctk.CTkButton(
            self,
            text="Iniciar nueva práctica",
            width=220,
            height=45
        )

        nueva.pack()