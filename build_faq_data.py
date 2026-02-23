"""
Parse FAQ.docx into Q&A pairs and generate audio files.
Output: faq_data.js (for chatbot) and audio/*.mp3
"""
import re
import json
from pathlib import Path
from docx import Document
from gtts import gTTS

ROOT = Path(__file__).parent
FAQ_PATH = ROOT / "FAQ.docx"
AUDIO_DIR = ROOT / "audio"
OUT_JS = ROOT / "faq_data.js"


def parse_faq(doc):
    """Extract list of {question, answer} from document paragraphs."""
    pairs = []
    current_q = None
    current_a = []

    def flush():
        if current_q is not None and (current_a or not pairs):
            answer = " ".join(current_a).strip()
            if answer or not pairs:
                pairs.append({"question": current_q.strip(), "answer": answer or "(No answer)"})

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        # Question: starts with optional number + ) or number + .
        if re.match(r"^\d+[).]\s*.+", text):
            flush()
            current_q = text
            current_a = []
        else:
            current_a.append(text)

    flush()
    return pairs


def main():
    doc = Document(FAQ_PATH)
    pairs = parse_faq(doc)

    AUDIO_DIR.mkdir(exist_ok=True)

    # Generate audio for each answer and build data with audio file path
    data = []
    for i, item in enumerate(pairs):
        q, a = item["question"], item["answer"]
        if not a:
            a = "(No answer)"
        audio_name = f"q{i + 1}.mp3"
        audio_path = AUDIO_DIR / audio_name
        print(f"Generating audio {i + 1}/{len(pairs)}: {q[:50]}...")
        tts = gTTS(text=a, lang="en", slow=False)
        tts.save(audio_path)
        data.append({"question": q, "answer": a, "audio": f"audio/{audio_name}"})

    # Write JavaScript file for HTML to include
    js_content = "const FAQ_DATA = " + json.dumps(data, indent=2) + ";\n"
    OUT_JS.write_text(js_content, encoding="utf-8")
    print(f"Written {OUT_JS} with {len(data)} FAQs. Audio in {AUDIO_DIR}/")


if __name__ == "__main__":
    main()
