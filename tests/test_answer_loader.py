from services.document_manager import DocumentManager
from services.answer_loader import AnswerLoader

manager = DocumentManager()
loader = AnswerLoader()

documentos = manager.get_all_documents()

for documento in documentos:
    print(documento.name)
    print(documento.answer)
    print("-" * 40)

if documentos:

    for documento in documentos:
        if documento.answer is not None:
            respuesta = loader.load(documento)
            print(respuesta)
            break


else:
    print("No hay documentos.")