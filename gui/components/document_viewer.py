import customtkinter as ctk
from PIL import Image


class DocumentViewer(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
        self,
        text="Documento",
        font=("Arial", 20, "bold")
        )

        self.title_label.grid(
            row=0,
            column=0,
            pady=10
        )

        self.image_label = ctk.CTkLabel(
            self,
            text="No hay documento cargado"
        )
        self.image_label.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.file_label = ctk.CTkLabel(
            self,
            text=""
        )
        self.file_label.grid(row=2, column=0, pady=10)

    def load_document(self, document):

        image = Image.open(document.image)

        image.thumbnail((500, 600))

        ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )

        self.image_label.configure(
            image=ctk_image,
            text=""
        )

        self.image_label.image = ctk_image

        self.file_label.configure(
            text=document.name
        )

    def set_progress_(self, current, total):
        self.title_label.configure(
            text=f"Documento {current} de {total}"
        )