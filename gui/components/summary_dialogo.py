import customtkinter as ctk


class SummaryDialog(ctk.CTkToplevel):

    def __init__(self, master, stats):
        super().__init__(master)

        self.title("Resumen de práctica")
        self.geometry("350x320")

        self.resizable(False, False)

        titulo = ctk.CTkLabel(
            self,
            text="Práctica finalizada",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=(20, 25))

        informacion = [
            f"Documentos: {stats.completed_documents}",
            f"Campos: {stats.total_fields}",
            f"Correctos: {stats.correct_fields}",
            f"Incorrectos: {stats.incorrect_fields}",
            f"Precisión: {stats.precision} %"
        ]

        for texto in informacion:

            etiqueta = ctk.CTkLabel(
                self,
                text=texto,
                font=("Arial", 16)
            )

            etiqueta.pack(pady=4)

        boton = ctk.CTkButton(
            self,
            text="Aceptar",
            command=self.destroy
        )

        boton.pack(pady=25)