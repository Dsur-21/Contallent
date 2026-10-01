import customtkinter as ctk

from services.users_manager import UsersManager


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master, on_start_practice):
        super().__init__(master)

        self.on_start_practice = on_start_practice

        self.users = UsersManager()

        self.grid_columnconfigure(0, weight=1)

        # =========================
        # TÍTULO
        # =========================

        titulo = ctk.CTkLabel(
            self,
            text="Bienvenido",
            font=("Arial", 28, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            pady=(30, 10)
        )

        descripcion = ctk.CTkLabel(
            self,
            text="Simulador profesional de captura documental.",
            font=("Arial", 18)
        )

        descripcion.grid(
            row=1,
            column=0,
            pady=(0, 20)
        )

        # =========================
        # USUARIO
        # =========================

        usuario_label = ctk.CTkLabel(
            self,
            text="Usuario",
            font=("Arial", 16, "bold")
        )

        usuario_label.grid(
            row=2,
            column=0,
            pady=(10, 5)
        )

        self.usuario_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Escribe tu usuario"
        )

        self.usuario_entry.grid(
            row=3,
            column=0,
            pady=(0, 10)
        )

        self.usuario_entry.bind(
            "<KeyRelease>",
            self.check_form
        )

        # =========================
        # INFORMACIÓN DEL USUARIO
        # =========================

        self.progreso_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 14),
            justify="center"
        )

        self.progreso_label.grid(
            row=4,
            column=0,
            pady=(0, 15)
        )

        # =========================
        # CANTIDAD DE DOCUMENTOS
        # =========================

        cantidad_label = ctk.CTkLabel(
            self,
            text="Cantidad de documentos",
            font=("Arial", 16, "bold")
        )

        cantidad_label.grid(
            row=5,
            column=0,
            pady=(0, 10)
        )

        self.cantidad_var = ctk.IntVar(
            value=5
        )

        self.cantidad_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "1",
                "5",
                "10",
                "15",
                "20"
            ],
            variable=self.cantidad_var
        )

        self.cantidad_menu.grid(
            row=6,
            column=0,
            pady=(0, 25)
        )

        # =========================
        # BOTÓN COMENZAR
        # =========================

        self.btn_comenzar = ctk.CTkButton(
            self,
            text="Comenzar práctica",
            width=220,
            height=45,
            state="disabled",
            command=self.start_practice
        )

        self.btn_comenzar.grid(
            row=7,
            column=0
        )

    # ==================================================
    # COMPROBAR USUARIO
    # ==================================================

    def check_form(self, event=None):

        usuario = self.usuario_entry.get().strip()

        if not usuario:

            self.btn_comenzar.configure(
                state="disabled"
            )

            self.progreso_label.configure(
                text=""
            )

            return

        self.btn_comenzar.configure(
            state="normal"
        )

        usuario_data = self.users.get_user(
            usuario
        )

        # =========================
        # USUARIO NUEVO
        # =========================

        if usuario_data is None:

            self.progreso_label.configure(
                text=(
                    "Usuario nuevo\n"
                    "Aún no tienes prácticas registradas."
                )
            )

            return

        # =========================
        # USUARIO EXISTENTE
        # =========================

        practices = usuario_data.get(
            "practices",
            0
        )

        documents = usuario_data.get(
            "documents",
            0
        )

        correct = usuario_data.get(
            "correct_fields",
            0
        )

        incorrect = usuario_data.get(
            "incorrect_fields",
            0
        )

        best_precision = usuario_data.get(
            "best_precision", 0
        )

        total_fields = correct + incorrect

        if total_fields > 0:

            precision = round(
                (correct / total_fields) * 100,
                2
            )

        else:

            precision = 0

        self.progreso_label.configure(
            text=(
                f"Bienvenido de nuevo, {usuario}\n\n"
                f"Prácticas realizadas: {practices}\n"
                f"Documentos completados: {documents}\n"
                f"Precisión acumulada: {precision}%\n"
                f"Mejor precisión: {best_precision}%"
            )
        )

    # ==================================================
    # COMENZAR PRÁCTICA
    # ==================================================

    def start_practice(self):

        usuario = self.usuario_entry.get().strip()

        if not usuario:
            return

        cantidad = int(
            self.cantidad_menu.get()
        )

        # Crear usuario si todavía no existe
        self.users.get_or_create_user(
            usuario
        )

        self.on_start_practice(
            usuario,
            cantidad
        )