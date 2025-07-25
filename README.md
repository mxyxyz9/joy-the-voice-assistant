# Jarvis - A Desktop Voice Assistant

A desktop voice assistant built with Python. It can understand voice commands to perform various tasks, from telling you the time to analyzing text using the Gemini API.

## Features

*   **Conversational UI:** Interacts with the user through voice commands and spoken responses.
*   **Information on Demand:**
    *   Tells the current time and date.
    *   Searches and summarizes articles from Wikipedia.
*   **Entertainment:**
    *   Plays music from your local library.
    *   Tells you jokes to lighten the mood.
*   **Productivity & System Tools:**
    *   Opens popular websites like Google and YouTube.
    *   Takes screenshots and saves them to your Pictures folder.
    *   Analyzes text from your clipboard using the Google Gemini API.
    *   Performs system shutdown and restart.
*   **Customization:**
    *   Allows you to change the assistant's name.

## Demo

*(You can add screenshots or a GIF of the assistant in action here. Here are some of the images already in your project's `Images` directory that you could use:)*

*   `Images/Cover_pic.jpg`
*   `Images/ss.png`
*   `Images/Picture1.png` through `Images/Picture11.png`

## Tech Stack

*   **Core Language:** Python 3
*   **Speech Recognition:** `SpeechRecognition`
*   **Text-to-Speech (TTS):** `pyttsx3`
*   **Web & API:** `requests`, `wikipedia`
*   **GUI Automation:** `PyAutoGUI`
*   **Utilities:** `pyjokes`, `python-dotenv`, `pyperclip`
*   **AI Integration:** Google Gemini API

## Setup and Installation

Follow these steps to get Jarvis running on your local machine.

### 1. Prerequisites

*   **Python 3.x:** Make sure Python is installed on your system. You can download it from [python.org](https://python.org/).
*   **Microphone:** A working microphone is required for voice commands.
*   **Google Gemini API Key:** The "analyze this" feature requires an API key. You can obtain a free one from [Google AI Studio](https://aistudio.google.com/app).

### 2. Clone the Repository

```bash
git clone https://github.com/mxyxyz9/Jarvis-Desktop-Voice-Assistant.git
cd Jarvis-Desktop-Voice-Assistant
```

### 3. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS and Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

### 4. Install Dependencies

Install all the required libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory of the project to store your API key.

1.  Create a new file named `.env`.
2.  Add the following line to the file, replacing `YOUR_API_KEY` with the key you obtained from Google AI Studio:
    ```
    GEMINI_API_KEY=YOUR_API_KEY
    ```

## How to Use

Once the setup is complete, you can run the assistant.

1.  Make sure your virtual environment is activated.
2.  Execute the main Python script:
    ```bash
    python Jarvis/jarvis.py
    ```
3.  The assistant will greet you and start listening for your commands.

### Available Voice Commands

*   "time"
*   "date"
*   "wikipedia [your query]"
*   "play music"
*   "open youtube"
*   "open google"
*   "change your name"
*   "screenshot"
*   "tell me a joke"
*   "analyze this" / "help me with this" (after copying text to the clipboard)
*   "shutdown"
*   "restart"
*   "offline" / "exit"

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mxyxyz9/Jarvis-Desktop-Voice-Assistant/issues).

## License

This project is licensed under the MIT License.

## Author

*   **mxyxyz9** - [GitHub Profile](https://github.com/mxyxyz9)
