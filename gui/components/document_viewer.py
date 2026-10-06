import customtkinter as ctk
from PIL import Image, ImageTk


class DocumentViewer(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tk_image = None
        self.image_id = None

        # =========================
        # TÍTULO
        # =========================

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

        # =========================
        # CONTENEDOR
        # =========================

        self.viewer_frame = ctk.CTkFrame(self)

        self.viewer_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=5
        )

        self.viewer_frame.grid_rowconfigure(0, weight=1)
        self.viewer_frame.grid_columnconfigure(0, weight=1)

        # =========================
        # CANVAS
        # =========================

        self.canvas = ctk.CTkCanvas(
            self.viewer_frame,
            highlightthickness=0
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # =========================
        # SCROLL VERTICAL
        # =========================

        self.scroll_y = ctk.CTkScrollbar(
            self.viewer_frame,
            orientation="vertical",
            command=self.canvas.yview
        )

        self.scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        # =========================
        # SCROLL HORIZONTAL
        # =========================

        self.scroll_x = ctk.CTkScrollbar(
            self.viewer_frame,
            orientation="horizontal",
            command=self.canvas.xview
        )

        self.scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.canvas.configure(
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set
        )

        # =========================
        # NOMBRE DEL ARCHIVO
        # =========================

        self.file_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.file_label.grid(
            row=2,
            column=0,
            pady=10
        )

        # Recentrar cuando cambie
        # el tamaño del visor
        self.canvas.bind(
            "<Configure>",
            self._center_image
        )

    # ==================================================
    # CARGAR DOCUMENTO
    # ==================================================

    def load_document(self, document):

        image = Image.open(
            document.image
        ).convert("RGB")

        max_width = 750
        max_height = 850

        image.thumbnail(
            (max_width, max_height),
            Image.Resampling.LANCZOS
        )


        self.tk_image = ImageTk.PhotoImage(image)

        # Limpiar imagen anterior
        self.canvas.delete("all")

        # Crear nueva imagen
        self.image_id = self.canvas.create_image(
            0,
            0,
            image=self.tk_image,
            anchor="center"
        )

        self.image_width = image.width
        self.image_height = image.height

        self.file_label.configure(
            text=document.name
        )

        self._center_image()

    # ==================================================
    # CENTRAR IMAGEN
    # ==================================================

    def _center_image(self, event=None):

        if self.image_id is None:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        image_width = self.image_width
        image_height = self.image_height

        x = canvas_width // 2
        y = canvas_height // 2

        if image_width > canvas_width:
            x = image_width // 2

        if image_height > canvas_height:
            y = image_height // 2

        self.canvas.coords(
            self.image_id,
            x,
            y
        )

        scroll_width = max(
            canvas_width,
            image_width
        )

        scroll_height = max(
            canvas_height,
            image_height
        )

        self.canvas.configure(
            scrollregion=(
                0,
                0,
                scroll_width,
                scroll_height
            )
        )

        if image_width <= canvas_width:
            self.canvas.xview_moveto(0)

        if image_height <= canvas_height:
            self.canvas.yview_moveto(0)

    # ==================================================
    # PROGRESO
    # ==================================================

    def set_progress(self, current, total):

        self.title_label.configure(
            text=f"Documento {current} de {total}"
        )


    def clear(self):

        self.canvas.delete("all")

        self.tk_image = None
        self.image_id = None

        self.title_label.configure(
            text="Documento"
        )

        self.file_label.configure(
            text=""
        )

        self.canvas.configure(
            scrollregion=(0, 0, 0, 0)
        )