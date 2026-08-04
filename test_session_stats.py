from services.session_stats import SessionStats

stats = SessionStats()

resultado = {
    "num_banc": False,
    "num_che": True,
    "nombre": True,
    "fecha": True,
    "importe": False,
    "elaboro": True,
    "concepto": False,
}

stats.update(resultado)

print("Documentos:", stats.completed_documents)
print("Correctos:", stats.correct_fields)
print("Incorrectos:", stats.incorrect_fields)
print("Total:", stats.total_fields)
print("Precisión:", stats.precision)

print("\nDetalle por campo:")
print(stats.field_stats)