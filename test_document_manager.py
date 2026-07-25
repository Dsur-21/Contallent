from services.document_manager import DocumentManager

manager = DocumentManager()

documento = manager.get_random_document()

print(documento)