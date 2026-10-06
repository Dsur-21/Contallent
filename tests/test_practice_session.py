from services.practice_session import PracticeSession

session = PracticeSession()

session.start()

print("Inicio de práctica\n")

while True:

    documento = session.next_document()

    if documento is None:
        break

    print(f"Nombre: {documento.name}")
    print(f"Tipo: {documento.document_type}")
    print(f"Imagen: {documento.image}")
    print(f"json: {documento.answer}")
    print("-"*40)
    

print("\nPráctica finalizada")