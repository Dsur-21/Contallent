from datetime import datetime
from decimal import Decimal, InvalidOperation


class Validator:

    def validate(self, expected, captured, usuario):

        result = {}

        result["num_banc"] = self.compare_text(
            expected.num_banc,
            captured.get("num_banc", "")
        )

        result["num_che"] = self.compare_text(
            expected.num_che,
            captured.get("num_che", "")
        )

        result["nombre"] = self.compare_text(
            expected.nombre,
            captured.get("nombre", "")
        )

        result["fecha"] = self.compare_date(
            expected.fecha,
            captured.get("fecha", "")
        )

        result["importe"] = self.compare_importe(
            expected.importe,
            captured.get("importe", "")
        )

        result["elaboro"] = (
            str(captured.get("elaboro", "")).strip()
            ==
            str(usuario).strip()
        )

        result["concepto"] = self.compare_text(
            expected.concepto,
            captured.get("concepto", "")
        )

        return result

    def compare_text(self, expected, captured):

        return (
            str(expected).strip().lower()
            ==
            str(captured).strip().lower()
        )

    def compare_importe(self, expected, captured):

        try:

            expected_value = Decimal(
                str(expected)
                .replace(",", "")
                .strip()
            )

            captured_value = Decimal(
                str(captured)
                .replace(",", "")
                .strip()
            )

            return expected_value == captured_value

        except (InvalidOperation, ValueError):

            return False


    def compare_date(self, expected, captured):

        formatos = [
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%Y/%m/%d",
            "%d.%m.%Y",
            "%Y.%m.%d"
        ]

        fecha_esperada = self.parse_date(
            expected,
            formatos
        )

        fecha_capturada = self.parse_date(
            captured,
            formatos
        )

        if fecha_esperada is None or fecha_capturada is None:
            return False

        return fecha_esperada == fecha_capturada

    def parse_date(self, value, formatos):

        value = str(value).strip()

        for formato in formatos:

            try:

                return datetime.strptime(
                    value,
                    formato
                ).date()

            except ValueError:
                continue

        return None