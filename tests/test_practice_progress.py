from services.practice_session import PracticeSession

session = PracticeSession()

session.start()

print("Total:", session.total_documents)

while True:

    documento = session.next_document()

    if documento is None:
        break

    print(
        f"Documento {session.current_document_number} de {session.total_documents}"
    )

print("Terminó:", session.is_finished())