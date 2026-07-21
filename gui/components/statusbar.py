import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=30)

        self.pack_propagate(False)

        estado = ctk.CTkLabel(
            self,
            text="Listo"
        )

        estado.pack(side="left", padx=10)