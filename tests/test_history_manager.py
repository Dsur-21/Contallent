from services.history_manager import HistoryManager
from services.session_stats import SessionStats

history = HistoryManager()

stats = SessionStats()

stats.completed_documents = 3
stats.correct_fields = 18
stats.incorrect_fields = 3

history.save(stats)

print(history.load_all())