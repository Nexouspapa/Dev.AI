import wikipedia
import os
import torch
import webbrowser
import speech_recognition as sr
from datetime import datetime
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

HF_TOKEN="<---your hf token--->"# Insert your Hugging Face token
CONVO_LOG = "conversation_log.txt"
login(HF_TOKEN)

#Voice Output 
def speak(text):
    print("Cristiano:", text)
    os.system(f"echo {text} | PowerShell -Command \"Add-Type –AssemblyName System.Speech; " +
              "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak([Console]::In.ReadToEnd())\"")

#Voice Input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("I'm having trouble with the speech service.")
        except Exception as e:
            speak(f"Error: {str(e)}")
        return None

#Load Mistral 
print("🔁 Loading Mistral model (may take time)...")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    torch_dtype=torch.float32,
    device_map="auto"
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Date & Time Functions 
def tell_time():
    return datetime.now().strftime("It's %I:%M %p")

def tell_date():
    return datetime.today().strftime("Today is %B %d, %Y")

# Website Shortcuts 
custom_commands = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "chatgpt": "https://chat.openai.com",
    "news": "https://news.google.com",
    "spotify": "https://open.spotify.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com"
}

# Conversation Logging 
def log_conversation(speaker, text):
    with open(CONVO_LOG, "a", encoding="utf-8") as file:
        file.write(f"{speaker}: {text}\n")

# Assistant Main Loop 
print("Cristiano AI 🤖 Ready! Say 'exit' to quit.")
speak("Hi, I am Cristiano. Ready to help you.")

while True:
    user_input = listen()
    if not user_input:
        continue

    log_conversation("You", user_input)
    user_input_lower = user_input.lower().strip()

    if "exit" in user_input_lower:
        response = "Goodbye!"
        speak(response)
        log_conversation("Cristiano", response)
        break

    # 🔗 Predefined website commands
    matched = False
    for keyword, url in custom_commands.items():
        if keyword in user_input_lower:
            response = f"Opening {keyword}."
            speak(response)
            log_conversation("Cristiano", response)
            webbrowser.open(url)
            matched = True
            break
    if matched:
        continue

    # 🔎 Google search
    if user_input_lower.startswith("search"):
        query = user_input_lower.replace("search", "").strip()
        if query:
            response = f"Searching {query} on Google."
            speak(response)
            log_conversation("Cristiano", response)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        continue

    # ▶️ YouTube play
    if user_input_lower.startswith("play"):
        query = user_input_lower.replace("play", "").strip()
        if query:
            response = f"Playing {query} on YouTube."
            speak(response)
            log_conversation("Cristiano", response)
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        continue

    # 🕒 Time and 📅 Date
    if "time" in user_input_lower:
        response = tell_time()
        speak(response)
        log_conversation("Cristiano", response)
        continue

    if "date" in user_input_lower:
        response = tell_date()
        speak(response)
        log_conversation("Cristiano", response)
        continue

    # 📚 General Knowledge Shortcuts
    gk_answers = {
        "who is the prime minister of india": "Narendra Modi is the current Prime Minister of India.",
        "who is the president of usa": "As of 2025, Joe Biden is the President of the United States.",
        "what is the capital of france": "The capital of France is Paris.",
        "who is cristiano ronaldo": "Cristiano Ronaldo is a Portuguese footballer widely regarded as one of the greatest players of all time.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"
    }
    for gk_question, gk_answer in gk_answers.items():
        if gk_question in user_input_lower:
            speak(gk_answer)
            log_conversation("Cristiano", gk_answer)
            break
    else:
        # Try AI-generated response
        prompt = f"<s>[INST] {user_input.strip()} [/INST]"
        print("Generating response...")
        try:
            response = generator(
                prompt,
                max_new_tokens=200,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )[0]['generated_text']

            reply = response[len(prompt):].strip()

            if not reply or "I'm just a language model" in reply.lower():
                raise ValueError("AI not helpful")

            speak(reply)
            log_conversation("Cristiano", reply)

        except Exception as e:
            print("AI failed, using Wikipedia:", e)
            try:
                summary = wikipedia.summary(user_input, sentences=2)
                speak(summary)
                log_conversation("Cristiano", summary)
            except Exception as wiki_err:
                fallback = "Sorry, I couldn't find an answer for that."
                speak(fallback)
                log_conversation("Cristiano", fallback)










