from gtts import gTTS
import os
with open("./text/file.txt", "r", encoding="utf-8") as file:
    text = file.read()
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)  # slow=False means normal speed
f_path = './speech/'
len_files =len([f for f in os.listdir(f_path) if os.path.isfile(os.path.join(f_path, f))])
tts.save(f"{f_path}crypto_update_{len_files + 1}.mp3")
