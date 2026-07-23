import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, on_change):
        super().__init__(master, width=220, corner_radius=0)

        self.on_change = on_change

        self.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self,
            text="Proyecto",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=(25, 40))

        opciones = [
            ("🏠 Inicio", "home"),
            ("📝 Nueva práctica", "captura"),
            ("📜 Historial", "historial"),
            ("⚙ Configuración", "configuracion")
        ]

        for texto, nombre in opciones:

            boton = ctk.CTkButton(
                self,
                text=texto,
                width=180,
                height=40,
                command=lambda n=nombre: self.on_change(n)
            )

            boton.pack(pady=8)