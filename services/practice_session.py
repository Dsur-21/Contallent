import random

from services.document_manager import DocumentManager


class PracticeSession:

    def __init__(self):

        self.document_manager = DocumentManager()

        self.documents = []

        self.current_index = -1

        self.started = False

    def start(self, cantidad=None):

        documentos = self.document_manager.get_all_documents()

        random.shuffle(documentos)

        if cantidad is not None:

            cantidad = min(
                cantidad,
                len(documentos)
            )

            documentos = documentos[:cantidad]

        self.documents = documentos

        self.current_index = -1

        self.started = True

    def next_document(self):

        if not self.started:
            return None

        self.current_index += 1

        if self.current_index >= len(self.documents):
            return None

        return self.documents[self.current_index]

    def current_document(self):

        if self.current_index < 0:
            return None

        if self.current_index >= len(self.documents):
            return None

        return self.documents[self.current_index]

    @property
    def total_documents(self):

        return len(self.documents)

    @property
    def current_document_number(self):

        if self.current_index < 0:
            return 0

        return self.current_index + 1

    @property
    def finished(self):

        return (
            self.started
            and self.current_index >= len(self.documents)
        )

    

    def reset(self):

        self.documents = []

        self.current_index = -1

        self.started = False