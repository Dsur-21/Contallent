import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self,
            text="Proyecto",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=(25, 40))

        botones = [
            "🏠 Inicio",
            "📝 Nueva práctica",
            "📜 Historial",
            "⚙ Configuración"
        ]

        for texto in botones:
            boton = ctk.CTkButton(
                self,
                text=texto,
                width=180,
                height=40
            )

            boton.pack(pady=8)