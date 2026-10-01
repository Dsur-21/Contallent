import json
from pathlib import Path


class UsersManager:

    def __init__(self):
        self.file = Path("database/users.json")
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self):
        if not self.file.exists():
            return {}

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_all(self, users):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

    def get_user(self, usuario):
        users = self.load_all()
        return users.get(usuario)

    def create_user(self, usuario):
        users = self.load_all()

        if usuario in users:
            return users[usuario]

        users[usuario] = {
            "user": usuario,
            "practices": 0,
            "documents": 0,
            "correct_fields": 0,
            "incorrect_fields": 0,
            "best_precision": 0
        }

        self.save_all(users)
        return users[usuario]

    def get_or_create_user(self, usuario):
        user = self.get_user(usuario)

        if user is not None:
            return user

        return self.create_user(usuario)

    def update_progress(self, usuario, stats):
        users = self.load_all()

        if usuario not in users:
            users[usuario] = {
                "user": usuario,
                "practices": 0,
                "documents": 0,
                "correct_fields": 0,
                "incorrect_fields": 0,
                "best_precision": 0
            }

        user = users[usuario]

        # Compatibilidad con usuarios ya registrados
        user.setdefault("best_precision", 0)

        user["practices"] += 1
        user["documents"] += stats.completed_documents
        user["correct_fields"] += stats.correct_fields
        user["incorrect_fields"] += stats.incorrect_fields

        # Actualizar la mejor precisión
        if stats.precision > user["best_precision"]:
            user["best_precision"] = stats.precision

        self.save_all(users)

        return user