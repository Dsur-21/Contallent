import customtkinter as ctk

from services.history_manager import HistoryManager


class HistorialFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.history = HistoryManager()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


        titulo = ctk.CTkLabel(
            self,
            text="Historial de prácticas",
            font=("Arial", 24, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            pady=(30, 20)
        )


        self.tabla = ctk.CTkScrollableFrame(
            self
        )

        self.tabla.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30,
            pady=10
        )


        botones = ctk.CTkFrame(self)

        botones.grid(
            row=2,
            column=0,
            pady=20
        )

        self.btn_actualizar = ctk.CTkButton(
            botones,
            text="Actualizar",
            command=self.load_history
        )

        self.btn_actualizar.pack(
            side="left",
            padx=10
        )

        self.btn_limpiar = ctk.CTkButton(
            botones,
            text="Limpiar historial",
            command=self.clear_history
        )

        self.btn_limpiar.pack(
            side="left",
            padx=10
        )

        self.load_history()

    def load_history(self):

        for widget in self.tabla.winfo_children():
            widget.destroy()

        history = self.history.load_all()

        if not history:

            mensaje = ctk.CTkLabel(
                self.tabla,
                text="No hay prácticas registradas.",
                font=("Arial", 16)
            )

            mensaje.pack(
                pady=40
            )

            return

        encabezados = [
            "Fecha",
            "Usuario",
            "Documentos",
            "Correctos",
            "Incorrectos",
            "Precisión"
        ]

        for columna, texto in enumerate(encabezados):

            label = ctk.CTkLabel(
                self.tabla,
                text=texto,
                font=("Arial", 14, "bold")
            )

            label.grid(
                row=0,
                column=columna,
                padx=15,
                pady=10,
                sticky="ew"
            )


        for fila, practica in enumerate(
            reversed(history),
            start=1
        ):

            datos = [
                practica.get("date", ""),
                practica.get("user", ""),
                practica.get("documents", 0),
                practica.get("correct_fields", 0),
                practica.get("incorrect_fields", 0),
                f"{practica.get('precision', 0)}%"
            ]

            for columna, dato in enumerate(datos):

                label = ctk.CTkLabel(
                    self.tabla,
                    text=str(dato),
                    font=("Arial", 13)
                )

                label.grid(
                    row=fila,
                    column=columna,
                    padx=15,
                    pady=8,
                    sticky="ew"
                )

        for columna in range(len(encabezados)):
            self.tabla.grid_columnconfigure(
                columna,
                weight=1
            )

    def clear_history(self):

        self.history.clear()

        self.load_history()