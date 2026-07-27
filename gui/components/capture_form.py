import customtkinter as ctk


class CaptureForm(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(1, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Captura del documento",
            font=("Arial", 22, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        self.entries = {}

        campos = [
            ("NUM BANC", "num_banc"),
            ("NUM CHE", "num_che"),
            ("NOMBRE", "nombre"),
            ("FECHA", "fecha"),
            ("IMPORTE", "importe"),
            ("ELABORÓ", "elaboro"),
            ("CONCEPTO", "concepto")
        ]

        for fila, (texto, clave) in enumerate(campos, start=1):

            etiqueta = ctk.CTkLabel(
                self,
                text=texto
            )

            etiqueta.grid(
                row=fila,
                column=0,
                padx=15,
                pady=8,
                sticky="w"
            )

            entrada = ctk.CTkEntry(
                self,
                height=34
            )

            entrada.grid(
                row=fila,
                column=1,
                padx=15,
                pady=8,
                sticky="ew"
            )

            self.entries[clave] = entrada

        self.btn_guardar = ctk.CTkButton(
            self,
            text="Guardar captura"
        )

        self.btn_guardar.grid(
            row=len(campos)+1,
            column=0,
            columnspan=2,
            pady=30
        )

    def clear(self):

        for entrada in self.entries.values():
            entrada.delete(0, "end")
