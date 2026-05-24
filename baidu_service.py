import base64
import json
import urllib.parse
import urllib.request


class BaiduAIService:
    """Call Baidu OCR and text-to-speech APIs."""

    TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token"
    OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    TTS_URL = "https://tsn.baidu.com/text2audio"

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Get Baidu access token by API Key and Secret Key."""
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_key,
        }
        url = self.TOKEN_URL + "?" + urllib.parse.urlencode(params)

        with urllib.request.urlopen(url, timeout=20) as response:
            result = json.loads(response.read().decode("utf-8"))

        if "access_token" not in result:
            raise RuntimeError(f"Failed to get access token: {result}")

        return result["access_token"]

    def recognize_text_from_image(self, image_path):
        """Recognize Chinese text from a local image."""
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        data = urllib.parse.urlencode({"image": image_base64}).encode("utf-8")
        url = self.OCR_URL + "?access_token=" + self.access_token

        request = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        if "words_result" not in result:
            raise RuntimeError(f"OCR request failed: {result}")

        lines = []
        for item in result["words_result"]:
            text = item.get("words", "").strip()
            if text:
                lines.append(text)

        return "\n".join(lines)

    def text_to_speech(self, text, output_path):
        """Convert text to MP3 speech by Baidu TTS."""
        params = {
            "tex": text,
            "tok": self.access_token,
            "cuid": "course_project_homework_1",
            "ctp": 1,
            "lan": "zh",
            "spd": 5,
            "pit": 5,
            "vol": 5,
            "per": 0,
            "aue": 3,
        }

        data = urllib.parse.urlencode(params).encode("utf-8")
        request = urllib.request.Request(self.TTS_URL, data=data, method="POST")

        with urllib.request.urlopen(request, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "")
            audio_data = response.read()

        if "audio" not in content_type:
            error_message = audio_data.decode("utf-8", errors="ignore")
            raise RuntimeError(f"TTS request failed: {error_message}")

        with open(output_path, "wb") as audio_file:
            audio_file.write(audio_data)
