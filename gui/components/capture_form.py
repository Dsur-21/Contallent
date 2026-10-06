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

    def get_data(self):

        return {
            key: entry.get().strip()
            for key, entry in self.entries.items()
        }

    def clear(self):

        for entrada in self.entries.values():
            entrada.delete(0, "end")

            entrada.configure(
                fg_color=("white", "gray20")
            )

    def show_validation(self, resultado):

        for campo, correcto in resultado.items():

            print(campo, correcto)

            if correcto:
                color = "#50BE66"
            else:
                color = "#F84B4B"

            self.entries[campo].configure(
                fg_color=color
            )