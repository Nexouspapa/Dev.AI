# Dev.AI
**DevAI** is an open-source, **voice-controlled AI assistant** designed to help users boost productivity and experience the future of intelligent interaction.   Internally, the assistant persona is named **Cristiano**, inspired by *Cristiano Ronaldo* — representing precision, speed, and greatness. ⚡

Cristiano listens, understands, and speaks back — performing web searches, Wikipedia queries, and task automation — powered by **Python**, **Hugging Face Transformers**, and **local voice control**.

---

## ✨ Key Features

- 🎙️ **Voice Recognition:** Hands-free command input using `speech_recognition`.
- 🗣️ **Text-to-Speech (TTS):** Realistic voice output via `pyttsx3` or PowerShell TTS.
- 🧠 **AI-Powered Conversations:** Dynamic, human-like replies via Hugging Face **Mistral-7B** model.
- 🌐 **Wikipedia Integration:** Instant factual summaries for general knowledge questions.
- ⚙️ **Custom Command Execution:** Opens apps, performs web searches, and automates routine tasks.
- 💾 **Conversation Logging:** Saves every conversation to `logs.txt` for tracking or debugging.
- 🧩 **Lightweight and Fast:** No GPU required — runs easily on standard laptops.
- 🔒 **Secure:** Uses `.env` for token management (never exposes your Hugging Face key).

---

## 🧰 Technologies Used

| Component | Technology / Tool |
|------------|-------------------|
| **Language Model** | Mistral-7B via Hugging Face Inference API |
| **Programming Language** | Python |
| **Voice Input** | `speech_recognition` |
| **Voice Output** | `pyttsx3`, PowerShell TTS |
| **Knowledge Integration** | Wikipedia API |
| **Automation** | `webbrowser` |
| **Environment Variables** | `python-dotenv` |
| **Model Hosting** | Hugging Face Inference API (Token Secured) |
| **Logging** | Plain `.txt` file |

---


**Flow Description:**
1. **User speaks** a command.
2. **Speech Recognition** transcribes audio into text.
3. **Command Processor** checks for predefined actions (e.g., “open YouTube”, “search Python tutorials”).
4. If no match, query is sent to **Hugging Face’s Mistral-7B** model for NLP-based reply.
5. If the API fails, **Wikipedia** provides a fallback summary.
6. **Text-to-Speech (TTS)** converts the reply back to voice.
7. Every interaction is saved in `logs.txt`.

---

## 💡 Why DevAI (Cristiano) is Useful

- 💻 **For Developers:** Automate web searches, open documentation, and access quick code explanations.
- 🧑‍🎓 **For Students:** Hands-free access to Wikipedia and AI-powered explanations.
- 🧓 **For Elderly Users:** Voice interface enables easy, natural interaction.
- 🏢 **For Professionals:** Quick information retrieval, task automation, and daily reminders.
- ⚙️ **For Hobbyists:** Fully customizable — add your own commands and APIs.

> 🏆 **Cristiano**, the voice within DevAI, is designed to respond like a mentor — quick, confident, and focused, just like the football legend himself ⚽.

---

## 🧠 Challenges Solved

✅ **No GPU Required:** All AI inference done via Hugging Face API  
✅ **Completely Voice-Based:** Local speech recognition and synthesis  
✅ **Lightweight Logging:** Simple `.txt` file for all conversations  
✅ **Reliable Fallbacks:** Combines LLM responses with Wikipedia search  
✅ **Modular Structure:** Easy to extend for IoT, home automation, or education use  

---



