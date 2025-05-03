from pypdf import PdfReader
import os 
# TURN ON VENV
path = os.getenv('MEDVITV2_PDF')
if path == None:
    raise ValueError("ERROR:")

reader = PdfReader(path)
pages = reader.pages
numb = int(input())
doc = [page.extract_text() for page in pages]
with open('./note.md', 'w', encoding='utf-8') as f:
    for idx, text in enumerate(doc):
        if idx < numb:
            f.write(text)
print(f'Number of pages: {len(reader.pages)}')
