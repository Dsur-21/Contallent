import customtkinter as ctk


class SummaryDialog(ctk.CTkToplevel):

    def __init__(self, master, stats):
        super().__init__(master)

        self.title("Resumen de práctica")
        self.geometry("350x320")

        self.resizable(False, False)


        self.transient(master)

        self.lift()
        self.focus_force()

        self.grab_set()

        self.update_idletasks()

        ancho = 350
        alto = 320

        ventana_ancho = master.winfo_width()
        ventana_alto = master.winfo_height()

        ventana_x = master.winfo_rootx()
        ventana_y = master.winfo_rooty()

        x = ventana_x + (ventana_ancho - ancho) // 2
        y = ventana_y + (ventana_alto - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

        # ==========================================
        # Contenido
        # ==========================================

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
            command=self.close
        )

        boton.pack(pady=25)

    def close(self):

        self.grab_release()
        self.destroy()