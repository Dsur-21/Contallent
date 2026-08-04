class SessionStats:

    def __init__(self):
        self.reset()

    def reset(self):

        self.completed_documents = 0

        self.correct_fields = 0
        self.incorrect_fields = 0

        self.field_stats = {
            "num_banc": {"correct": 0, "incorrect": 0},
            "num_che": {"correct": 0, "incorrect": 0},
            "nombre": {"correct": 0, "incorrect": 0},
            "fecha": {"correct": 0, "incorrect": 0},
            "importe": {"correct": 0, "incorrect": 0},
            "elaboro": {"correct": 0, "incorrect": 0},
            "concepto": {"correct": 0, "incorrect": 0},
        }
 
    def update(self, resultado):

        self.completed_documents += 1

        for campo, correcto in resultado.items():

            if correcto:
                self.correct_fields += 1
                self.field_stats[campo]["correct"] += 1
            else:
                self.incorrect_fields += 1
                self.field_stats[campo]["incorrect"] += 1

    @property
    def total_fields(self):
        return self.correct_fields + self.incorrect_fields

    @property
    def precision(self):

        if self.total_fields == 0:
            return 0

        return round(
            (self.correct_fields / self.total_fields) * 100,
            2
        )