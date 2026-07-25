from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    """
    Representa un documento de práctica.
    """

    image: Path
    answer: Path | None
    document_type: str

    @property
    def name(self):
        return self.image.name