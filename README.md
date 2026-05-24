# Homework 1: Intelligent Image Text Broadcasting Assistant

This project is for **人工智能系统管理与应用 - 大作业1**.

The program reads a local image, recognizes the text in the image using **Baidu OCR**, converts the recognized text into speech using **Baidu TTS**, saves the text result, saves an MP3 file, and plays the audio.

## Files

| File | Purpose |
|---|---|
| `config.py` | Stores your Baidu API Key, Secret Key, image path, and output paths. |
| `baidu_service.py` | Contains the Baidu OCR and TTS API code. |
| `main.py` | Main program. Run this file. |
| `sample_image.png` | Your input image. You need to add this file yourself. |
| `recognized_text.txt` | Output text file generated after running the program. |
| `broadcast_result.mp3` | Output audio file generated after running the program. |

## Before Running

1. Create or open your Baidu AI application.
2. Make sure the application has these services enabled:
   - **文字识别 OCR**
   - **语音合成 TTS**
3. Open `config.py`.
4. Replace:

```python
API_KEY = "PASTE_YOUR_API_KEY_HERE"
SECRET_KEY = "PASTE_YOUR_SECRET_KEY_HERE"
```

with your real Baidu API Key and Secret Key.

5. Put your test image in this folder and name it:

```text
sample_image.png
```

## How to Run

Open PowerShell or PyCharm terminal in this folder and run:

```powershell
python main.py
```

## Expected Result

After running successfully, the program will create:

```text
recognized_text.txt
broadcast_result.mp3
```

The console will also print the OCR result.

## Common Error

If you see:

```text
No permission to access data
```

it means your API Key exists, but the Baidu application does not have permission for the service you are calling. For this project, enable **文字识别 OCR** and **语音合成 TTS** in the Baidu console.
