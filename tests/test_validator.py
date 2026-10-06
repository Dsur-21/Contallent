from services.validator import Validator

validator = Validator()

correcto = {
    "nombre": "BBVA",
    "importe": "2500",
    "concepto": "Pago proveedor"
}

usuario = {
    "nombre": "bbva",
    "importe": "2500",
    "concepto": "Pago Proveedor"
}

resultado = validator.validate(correcto, usuario)

print(resultado)