"""Extract text from FAQ.docx to understand structure."""
from docx import Document
from pathlib import Path

path = Path(__file__).parent / "FAQ.docx"
doc = Document(path)
for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if text:
        print(f"[{i}] {text[:100]}{'...' if len(text) > 100 else ''}")
