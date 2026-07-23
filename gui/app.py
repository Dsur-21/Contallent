import customtkinter as ctk

from gui.components.sidebar import Sidebar
from gui.components.header import Header
from gui.components.statusbar import StatusBar

from gui.home import HomeFrame
from gui.captura import CapturaFrame
from gui.historial import HistorialFrame
from gui.configuracion import ConfiguracionFrame


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Proyecto Captura Contable")
        self.geometry("1200x700")

        # ===== Sidebar =====
        self.sidebar = Sidebar(self, self.show_frame)
        self.sidebar.pack(side="left", fill="y")

        # ===== Área derecha =====
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Header
        self.header = Header(self.right_frame)
        self.header.pack(fill="x")

        # Contenedor de pantallas
        self.content = ctk.CTkFrame(self.right_frame)
        self.content.pack(fill="both", expand=True)

        # StatusBar
        self.status = StatusBar(self.right_frame)
        self.status.pack(fill="x", side="bottom")

        # Diccionario de pantallas
        self.frames = {}

        self.frames["home"] = HomeFrame(self.content)
        self.frames["captura"] = CapturaFrame(self.content)
        self.frames["historial"] = HistorialFrame(self.content)
        self.frames["configuracion"] = ConfiguracionFrame(self.content)

        self.current_frame = None

        self.show_frame("home")

    def show_frame(self, frame_name):

        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.current_frame = self.frames[frame_name]    

        self.current_frame.pack(fill="both", expand=True)