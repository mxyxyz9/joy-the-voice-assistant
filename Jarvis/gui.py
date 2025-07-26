import customtkinter
from jarvis import takecommand, speak
import threading

class JarvisGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jarvis Voice Assistant")
        self.geometry("500x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(self, width=480, height=500)
        self.textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.listen_button = customtkinter.CTkButton(self, text="Listen", command=self.listen_thread)
        self.listen_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def listen_thread(self):
        thread = threading.Thread(target=self.listen)
        thread.start()

    def listen(self):
        self.textbox.insert("end", "Listening...\n")
        query = takecommand()
        if query:
            self.textbox.insert("end", f"You: {query}\n")
            # This is a placeholder for the response
            response = f"Jarvis: I heard you say '{query}'"
            self.textbox.insert("end", f"{response}\n")
            speak(response)

if __name__ == "__main__":
    app = JarvisGUI()
    app.mainloop()
