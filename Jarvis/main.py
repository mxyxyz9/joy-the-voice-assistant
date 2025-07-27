import jarvis

if __name__ == '__main__':
    jarvis.wishme()

    while True:
        query = jarvis.takecommand()
        if not query:
            continue

        if "time" in query:
            jarvis.time()
            
        elif "date" in query:
            jarvis.date()

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            jarvis.search_wikipedia(query)

        elif "play music" in query:
            song_name = query.replace("play music", "").strip()
            jarvis.play_music(song_name)

        elif "open youtube" in query:
            jarvis.wb.open("youtube.com")
            
        elif "open google" in query:
            jarvis.wb.open("google.com")

        elif "change your name" in query:
            jarvis.set_name()

        elif "screenshot" in query:
            jarvis.screenshot()
            jarvis.speak("I've taken screenshot, please check it")

        elif "tell me a joke" in query:
            joke = jarvis.pyjokes.get_joke()
            jarvis.speak(joke)
            print(joke)
            
        elif "analyze this" in query or "help me with this" in query:
            clipboard_content = jarvis.pyperclip.paste()
            if clipboard_content:
                response = jarvis.get_gemini_response(f"Analyze this code: {clipboard_content}")
                jarvis.speak(response)
            else:
                jarvis.speak("The clipboard is empty. Please copy something to the clipboard first.")

        elif "shutdown" in query:
            jarvis.speak("Shutting down the system, goodbye!")
            jarvis.os.system("shutdown /s /f /t 1")
            break
            
        elif "restart" in query:
            jarvis.speak("Restarting the system, please wait!")
            jarvis.os.system("shutdown /r /f /t 1")
            break
            
        elif "offline" in query or "exit" in query:
            jarvis.speak("Going offline. Have a good day!")
            break
