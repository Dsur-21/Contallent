from pathlib import Path
import random

from models.document import Document

class DocumentManager:

    def __init__(self):

        self.base_path = Path("assets/documents")

        self.extensions = (
            "*.png",
            "*.jpg",
            "*.jpeg",
            "*.bmp"
        )

    def get_all_documents(self):

        documentos = []

        for extension in self.extensions:
            for image_path in self.base_path.rglob(extension):

                document_type = image_path.parent.name

                answer_path = image_path.with_suffix(".json")

                if not answer_path.exists():
                    answer_path = None

                documentos.append(
                    Document(
                        image = image_path,
                        answer = answer_path,
                        document_type = document_type
                    )
                )

        return documentos

    def get_random_document(self):

        documentos = self.get_all_documents()

        if not documentos:
            return None

        return random.choice(documentos)