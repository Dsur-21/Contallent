from dataclasses import asdict
from models.answer import Answer

class Validator:

    def validate(self, expected, captured: dict):

        expected = asdict(expected)

        result = {}

        for field, expected_value in expected.items():

            user_value = captured.get(field, "")

            result[field] = (
                str(user_value).strip().lower()
                ==
                str(expected_value).strip().lower()
            )

        return result