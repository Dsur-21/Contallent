import json

from models import Answer


class AnswerLoader:

    def load(self, document):

        if document.answer is None:
            return None

        with open(document.answer, encoding="utf-8") as file:

            data = json.load(file)

        return Answer(**data)