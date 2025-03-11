import os
import random
import string
import gtts
import langdetect
from playsound import playsound

# ✅ Ensure 'temp_audio' directory exists
current_dir = os.path.dirname(os.path.abspath(__file__))
temp_audio_dir = os.path.join(current_dir, "temp_audio")
os.makedirs(temp_audio_dir, exist_ok=True)

def generate_random_filename():
    """ Generate a random filename to prevent overwriting. """
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return os.path.join(temp_audio_dir, f"output_{random_string}.mp3")

def detect_language(text):
    """ Detects language and maps it to a supported TTS language code. """
    try:
        lang_code = langdetect.detect(text)
        supported_languages = {"en": "en", "hi": "hi", "mr": "mr"}
        return supported_languages.get(lang_code, "en")  # Default to English if not supported
    except langdetect.lang_detect_exception.LangDetectException:
        return "en"  # Default to English on error

def text_to_speech():
    try:
        text = input("\n🔹 Enter text (Hindi, Marathi, or English): ").strip()
        if not text:
            print("❌ Error: No text entered!")
            return
        
        # ✅ Improved language detection
        language = detect_language(text)
        print(f"🌍 Detected Language: {language}")

        # Convert text to speech
        tts = gtts.gTTS(text=text, lang=language)
        output_file = generate_random_filename()
        tts.save(output_file)

        print(f"✅ Speech saved! Playing now: {output_file}")

        # ✅ FIXED: Use os.system() instead of playsound (Windows fix)
        os.system(f'start /min "" "{output_file}"')

    except Exception as e:
        print(f"❌ Error in text-to-speech conversion: {e}")

if __name__ == "__main__":
    while True:
        text_to_speech()
        again = input("\n🔄 Convert another text? (y/n): ").strip().lower()
        if again != "y":
            break

    print("✅ Exiting program.")
