import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import jarvis

class JarvisGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jarvis - Your Voice Assistant")
        self.geometry("800x600")
        self.resizable(False, False)

        # Set the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Create the main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Create the title label
        self.title_label = ctk.CTkLabel(self.main_frame, text="Jarvis", font=ctk.CTkFont(size=30, weight="bold"))
        self.title_label.pack(pady=20)

        # Create the conversation text box
        self.conversation_text = ctk.CTkTextbox(self.main_frame, width=700, height=400, corner_radius=10, font=ctk.CTkFont(size=14))
        self.conversation_text.pack(pady=10, padx=10)

        # Create the status label
        self.status_label = ctk.CTkLabel(self.main_frame, text="Status: Idle", font=ctk.CTkFont(size=16))
        self.status_label.pack(pady=10)

        # Create the start/stop button
        self.start_stop_button = ctk.CTkButton(self.main_frame, text="Start Assistant", command=self.toggle_assistant, font=ctk.CTkFont(size=16, weight="bold"))
        self.start_stop_button.pack(pady=20)

        self.assistant_running = False

    def toggle_assistant(self):
        if self.assistant_running:
            self.assistant_running = False
            self.start_stop_button.configure(text="Start Assistant")
            self.status_label.configure(text="Status: Idle")
        else:
            self.assistant_running = True
            self.start_stop_button.configure(text="Stop Assistant")
            self.status_label.configure(text="Status: Listening...")
            self.run_assistant()

    def run_assistant(self):
        if self.assistant_running:
            query = jarvis.takecommand()
            if query:
                self.conversation_text.insert("end", f"You: {query}\n")
                self.handle_query(query)
            self.after(100, self.run_assistant)

    def handle_query(self, query):
        if "time" in query:
            response = jarvis.time()
        elif "date" in query:
            response = jarvis.date()
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            response = jarvis.search_wikipedia(query)
        elif "play music" in query:
            song_name = query.replace("play music", "").strip()
            response = jarvis.play_music(song_name)
        elif "open youtube" in query:
            jarvis.wb.open("youtube.com")
            response = "Opening YouTube..."
        elif "open google" in query:
            jarvis.wb.open("google.com")
            response = "Opening Google..."
        elif "change your name" in query:
            response = jarvis.set_name()
        elif "screenshot" in query:
            jarvis.screenshot()
            response = "I've taken a screenshot, please check it."
        elif "tell me a joke" in query:
            response = jarvis.pyjokes.get_joke()
        elif "analyze this" in query or "help me with this" in query:
            clipboard_content = jarvis.pyperclip.paste()
            if clipboard_content:
                response = jarvis.get_gemini_response(f"Analyze this code: {clipboard_content}")
            else:
                response = "The clipboard is empty. Please copy something to the clipboard first."
        elif "shutdown" in query:
            jarvis.speak("Shutting down the system, goodbye!")
            jarvis.os.system("shutdown /s /f /t 1")
            self.quit()
        elif "restart" in query:
            jarvis.speak("Restarting the system, please wait!")
            jarvis.os.system("shutdown /r /f /t 1")
            self.quit()
        elif "offline" in query or "exit" in query:
            jarvis.speak("Going offline. Have a good day!")
            self.quit()
        else:
            response = "I'm sorry, I don't know how to handle that command."

        self.conversation_text.insert("end", f"Jarvis: {response}\n")
        jarvis.speak(response)

if __name__ == "__main__":
    app = JarvisGUI()
    app.mainloop()
