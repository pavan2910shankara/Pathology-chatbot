"""
Text to Audio - Converts text to MP3 audio files using Google Text-to-Speech.
"""

from gtts import gTTS
from pathlib import Path
import sys


def text_to_audio(text: str, output_path: str = "output.mp3", lang: str = "en", slow: bool = False) -> str:
    """
    Convert text to an audio file (MP3).

    Args:
        text: The text to speak.
        output_path: Where to save the audio file (default: output.mp3).
        lang: Language code (default: "en" for English). Examples: "hi" (Hindi), "te" (Telugu).
        slow: If True, speaks slowly.

    Returns:
        Path to the created audio file.
    """
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(output_path)
    return str(Path(output_path).resolve())


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python text_to_audio.py \"Your text here\" [output.mp3] [lang]")
        print("  python text_to_audio.py --file input.txt [output.mp3] [lang]")
        print("Example: python text_to_audio.py \"Hello world\" hello.mp3 en")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Provide a file path: python text_to_audio.py --file input.txt")
            sys.exit(1)
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            text = f.read()
        output = sys.argv[3] if len(sys.argv) > 3 else "output.mp3"
        lang = sys.argv[4] if len(sys.argv) > 4 else "en"
    else:
        text = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else "output.mp3"
        lang = sys.argv[3] if len(sys.argv) > 3 else "en"

    path = text_to_audio(text, output_path=output, lang=lang)
    print(f"Audio saved to: {path}")


if __name__ == "__main__":
    main()
