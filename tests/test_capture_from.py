from gui.components.capture_form import CaptureForm
import customtkinter as ctk

app = ctk.CTk()

form = CaptureForm(app)
form.pack(fill="both", expand=True)

app.mainloop()