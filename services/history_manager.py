import json
from datetime import datetime
from pathlib import Path

class HistoryManager:

    def __init__(self):
        self.file = Path("database/history.json")


    def save(self, stats, usuario):

        if stats.completed_documents == 0:
            return

        if self.file.exists():

            with open(self.file,"r", encoding="utf-8") as f:
                history = json.load(f)

        else:
            history = []

        history.append(
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": usuario,
                "documents": stats.completed_documents,
                "correct_fields": stats.correct_fields,
                "incorrect_fields": stats.incorrect_fields,
                "precision": stats.precision
            }
        )

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                history,
                f,
                indent=4,
                ensure_ascii=False
            )

    def load_all(self):

        if not self.file.exists():
            return []

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def clear(self):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([], f)
