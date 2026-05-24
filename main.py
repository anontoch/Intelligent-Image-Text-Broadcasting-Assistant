import os
import sys

from baidu_service import BaiduAIService
from config import API_KEY, AUDIO_OUTPUT_PATH, IMAGE_PATH, SECRET_KEY, TEXT_OUTPUT_PATH


def play_audio(audio_path):
    """Play generated MP3 file on Windows."""
    if os.path.exists(audio_path):
        os.startfile(audio_path)
    else:
        print("Audio file was not found.")


def main():
    if API_KEY == "PASTE_YOUR_API_KEY_HERE" or SECRET_KEY == "PASTE_YOUR_SECRET_KEY_HERE":
        print("Please fill in your API Key and Secret Key in config.py first.")
        return

    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found: {IMAGE_PATH}")
        print("Put your image in this folder and name it sample_image.png.")
        return

    service = BaiduAIService(API_KEY, SECRET_KEY)

    print("Reading image and calling Baidu OCR...")
    recognized_text = service.recognize_text_from_image(IMAGE_PATH)

    print("\nOCR Result:")
    print(recognized_text)

    with open(TEXT_OUTPUT_PATH, "w", encoding="utf-8") as text_file:
        text_file.write(recognized_text)

    print(f"\nText result saved to: {TEXT_OUTPUT_PATH}")

    speech_text = "图片中的文字内容为：" + recognized_text
    print("Calling Baidu TTS and generating MP3...")
    service.text_to_speech(speech_text, AUDIO_OUTPUT_PATH)

    print(f"Audio result saved to: {AUDIO_OUTPUT_PATH}")
    play_audio(AUDIO_OUTPUT_PATH)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
