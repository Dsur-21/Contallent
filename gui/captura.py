import customtkinter as ctk

from gui.components.document_viewer import DocumentViewer
from gui.components.capture_form import CaptureForm

from services.practice_session import PracticeSession
from services.session_stats import SessionStats
from services.answer_loader import AnswerLoader
from services.validator import Validator
from gui.components.summary_dialogo import SummaryDialog

class CapturaFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.practice_session = PracticeSession()

        self.answer_loader = AnswerLoader()
        self.validator = Validator()
        self.stats = SessionStats()


        self.current_document = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.btn_nueva_practica = ctk.CTkButton(
            self,
            text = "Nueva práctica",
            command = self.start_practice
        )

        self.btn_nueva_practica.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            pady = (0, 15)
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

    def start_practice(self):
        self.stats.reset()

        self.practice_session.start()
        
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
            captura
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

            SummaryDialog(self, self.stats)  
            print("Documentos:", self.stats.completed_documents)
            print("Campos:", self.stats.total_fields)
            print("Correctos:",self.stats.correct_fields)
            print("Incorrectos:", self.stats.incorrect_fields)
            print("Precisión:", self.stats.precision, "%")

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
