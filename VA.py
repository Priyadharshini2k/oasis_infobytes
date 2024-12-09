import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet():
    """Greets the user."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def get_audio():
    """Captures audio input from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service.")
            return None

def process_query(query):
    """Processes the user's query and performs actions."""
    if "hello" in query:
        speak("Hello! How can I help you?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in query:
        speak("What should I search for?")
        search_query = get_audio()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the results for {search_query}")
    else:
        speak("I am not sure how to respond to that.")

# Main program
if __name__ == "__main__":
    speak("Starting voice assistant...")
    greet()
    while True:
        query = get_audio()
        if query:
            if "exit" in query or "bye" in query:
                speak("Goodbye! Have a great day!")
                break
            process_query(query)
