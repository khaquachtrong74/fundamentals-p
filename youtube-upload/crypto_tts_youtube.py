
import os
import datetime
import requests
import subprocess
import pickle
from google.cloud import texttospeech
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# --- Step 1: Fetch Crypto Data ---
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from CoinGecko")

# --- Step 2: Generate Update Text ---
def generate_update_text(data):
    now = datetime.datetime.now()
    time_str = now.strftime("%I %p").lstrip('0')

    btc = data["bitcoin"]
    eth = data["ethereum"]
    sol = data["solana"]

    changes = {
        "Bitcoin": btc["usd_24h_change"],
        "Ethereum": eth["usd_24h_change"],
        "Solana": sol["usd_24h_change"]
    }

    top_gainer = max(changes, key=changes.get)
    top_change = changes[top_gainer]

    return (
        f"Here's your {time_str} crypto update. "
        f"Bitcoin is at ${btc['usd']:,.2f}, "
        f"Ethereum at ${eth['usd']:,.2f}. "
        f"Top gainer: {top_gainer}, up {top_change:.2f} percent today."
    )

# --- Step 3: TTS using Google Cloud ---
def synthesize_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

# --- Step 4: Convert MP3 to MP4 with Static Image ---
def create_video(mp3_path, image_path, output_path):
    subprocess.run([
        "ffmpeg",
        "-loop", "1",
        "-i", image_path,
        "-i", mp3_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-pix_fmt", "yuv420p",
        output_path
    ])

# --- Step 5: Upload to YouTube ---
def upload_to_youtube(video_file, title, description, tags):
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "28"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = request.execute()
    print("Video uploaded: https://youtube.com/watch?v=" + response["id"])

# --- Main Orchestration ---
def main():
    try:
        data = fetch_crypto_data()
        text = generate_update_text(data)
        audio_file = "crypto_update.mp3"
        video_file = "crypto_update.mp4"
        background_image = "background.jpg"  # Use any image you want

        synthesize_speech(text, audio_file)
        create_video(audio_file, background_image, video_file)

        upload_to_youtube(
            video_file,
            title="Crypto Update - " + datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            description="Auto-generated crypto market update. Powered by AI.",
            tags=["crypto", "bitcoin", "ethereum", "solana", "market update"]
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
