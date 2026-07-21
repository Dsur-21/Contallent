import customtkinter as ctk

from gui.components.sidebar import Sidebar
from gui.components.header import Header
from gui.components.statusbar import StatusBar


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Proyecto")
        self.geometry("1200x700")

        # Menú lateral
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # Contenedor derecho
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Encabezado
        self.header = Header(self.right_frame)
        self.header.pack(fill="x")

        # Área de trabajo
        self.content = ctk.CTkFrame(self.right_frame)
        self.content.pack(fill="both", expand=True)

        mensaje = ctk.CTkLabel(
            self.content,
            text="Bienvenido",
            font=("Arial", 28, "bold")
        )
        mensaje.pack(pady=60)

        # Barra de estado
        self.status = StatusBar(self.right_frame)
        self.status.pack(fill="x", side="bottom")