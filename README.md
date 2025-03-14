# NLP Text-to-Speech Project
A simple Python project that converts text (Hindi, Marathi, and English) into speech using Google Text-to-Speech (gTTS) and Pydub for audio processing.

✅ Converts Hindi, Marathi, and English text into speech
✅ Automatically detects language
✅ Saves generated speech as an MP3 file
✅ Plays the generated speech
✅ Works without an internet connection after installation

NLP_text-to-speech/
│── scripts/
│   ├── main.py            # Main script
│   ├── language_detect.py # Language detection logic
│── temp_audio/            # Temporary audio storage
│── ffmpeg/                # FFmpeg binaries for audio processing
│── requirements.txt       # Required dependencies
│── README.md              # Project Documentation


Clone the Repository:
git clone https://github.com/your-username/NLP_text-to-speech.git
cd NLP_text-to-speech

Create and Activate Virtual Environment:
python -m venv venv

For windows:
venv\Scripts\activate

On Mac/Linux:
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

License:
This project is open-source and available under the MIT License.