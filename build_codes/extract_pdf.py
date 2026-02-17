import PyPDF2

reader = PyPDF2.PdfReader(r'd:\KUET CSE-2K21\3-2\mobile_presentation\UnifiedExperienceDesign_BookChapterfinal.pdf')
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        print(f'=== PAGE {i+1} ===')
        print(text)
        print()
