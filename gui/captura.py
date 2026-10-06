import customtkinter as ctk

from gui.components.summary_dialogo import SummaryDialog
from gui.components.document_viewer import DocumentViewer
from gui.components.capture_form import CaptureForm

from services.practice_session import PracticeSession
from services.history_manager import HistoryManager
from services.users_manager import UsersManager
from services.session_stats import SessionStats
from services.answer_loader import AnswerLoader
from services.validator import Validator

class CapturaFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.practice_session = PracticeSession()
        self.answer_loader = AnswerLoader()
        self.history = HistoryManager()
        self.users = UsersManager()
        self.validator = Validator()
        self.stats = SessionStats()


        self.current_document = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.btn_finalizar = ctk.CTkButton(
            self,
            text="Finalizar práctica",
            command=self.finish_practice,
            state="disabled"
        )

        self.btn_finalizar.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

        self.viewer = DocumentViewer(self)
        self.viewer.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)


        self.formulario = CaptureForm(self)
        self.formulario.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        self.formulario.btn_guardar.configure(
            command=self.validate_capture
        )

        self.btn_siguiente = ctk.CTkButton(
            self,
            text="Siguiente documento",
            command=self.next_document,
            state="disabled"
        )

        self.btn_siguiente.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

    def start_practice(self, usuario=None, cantidad=None):

        self.usuario = usuario
        self.cantidad_documentos = cantidad

        self.stats.reset()

        self.practice_session.start(cantidad)

        documento = self.practice_session.next_document()

        if documento:

            self.current_document = documento

            self.viewer.load_document(documento)

            self.viewer.set_progress(
                self.practice_session.current_document_number,
                self.practice_session.total_documents
            )

            self.formulario.clear()

            self.formulario.btn_guardar.configure(
                state="normal"
            )

            self.btn_siguiente.configure(
                state="disabled"
            )

            self.btn_finalizar.configure(
                state="normal"
            )

    def validate_capture(self):

        if self.current_document is None:
            print("No hay práctica iniciada.")
            return

        captura = self.formulario.get_data()

        respuesta = self.answer_loader.load(
            self.current_document
        )

        print("Captura:")
        print(captura)

        print("\nRespuesta:")
        print(respuesta)

        if respuesta is None:
            print("\nEste documento no tiene archivo de respuestas.")
            return

        resultado = self.validator.validate(
            respuesta,
            captura,
            self.usuario
        )

        print("\nResultado:")
        print(resultado)

        self.formulario.show_validation(resultado)

        self.stats.update(resultado)

        print("\n=== Estadísticas ===")
        print("Documentos:", self.stats.completed_documents)
        print("Correctos:", self.stats.correct_fields)
        print("Incorrectos:", self.stats.incorrect_fields)
        print("Precisión:", self.stats.precision)

        self.formulario.btn_guardar.configure(
            state="disabled"
        )

        self.btn_siguiente.configure(
            state="normal"
        )

    def next_document(self):

        documento = self.practice_session.next_document()

        if documento is None:

            self.current_document = None

            self.formulario.btn_guardar.configure(
                state="disabled"
            )

            self.btn_siguiente.configure(
                state="disabled"
            )

            self.btn_finalizar.configure(
                state="disabled"
            )

            self.history.save(self.stats, self.usuario)

            self.users.update_progress(
                self.usuario,
                self.stats
            )

            SummaryDialog(
                self,
                self.stats
            )

            return

        self.current_document = documento

        self.viewer.load_document(documento)

        self.viewer.set_progress(
            self.practice_session.current_document_number,
            self.practice_session.total_documents
        )

        self.formulario.clear()

        self.formulario.btn_guardar.configure(
            state="normal"
        )

        self.btn_siguiente.configure(
            state="disabled"
        )

    def finish_practice(self):

        if self.current_document is None:
            return

        confirmar = ctk.CTkToplevel(self)

        confirmar.title("Finalizar práctica")
        confirmar.geometry("400x220")

        confirmar.transient(self)
        confirmar.grab_set()

        titulo = ctk.CTkLabel(
            confirmar,
            text="¿Finalizar práctica?",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=(25, 10))

        mensaje = ctk.CTkLabel(
            confirmar,
            text=(
                f"Has completado "
                f"{self.stats.completed_documents} de "
                f"{self.practice_session.total_documents} documentos.\n\n"
                "¿Deseas finalizar la práctica?"
            ),
            justify="center"
        )

        mensaje.pack(pady=10)

        botones = ctk.CTkFrame(confirmar)
        botones.pack(pady=15)

        btn_cancelar = ctk.CTkButton(
            botones,
            text="Cancelar",
            command=confirmar.destroy
        )

        btn_cancelar.grid(
            row=0,
            column=0,
            padx=10
        )

        btn_finalizar = ctk.CTkButton(
            botones,
            text="Finalizar",
            command=lambda: self.confirm_finish(confirmar)
        )

        btn_finalizar.grid(
            row=0,
            column=1,
            padx=10
        )


    def confirm_finish(self, ventana):

        ventana.destroy()

        self.current_document = None

        self.formulario.btn_guardar.configure(
            state="disabled"
        )

        self.btn_siguiente.configure(
            state="disabled"
        )

        self.btn_finalizar.configure(
            state="disabled"
        )

        self.history.save(
            self.stats,
            self.usuario
        )

        self.users.update_progress(
            self.usuario,
            self.stats
        )

        SummaryDialog(
            self,
            self.stats
        )


    def reset_practice(self):

        self.practice_session.reset()

        self.stats.reset()

        self.current_document = None

        self.formulario.clear()

        self.viewer.clear()

        # Deshabilitar botones
        self.formulario.btn_guardar.configure(
            state="disabled"
        )

        self.btn_siguiente.configure(
            state="disabled"
        )