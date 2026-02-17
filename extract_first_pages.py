import PyPDF2

reader = PyPDF2.PdfReader(r'd:\KUET CSE-2K21\3-2\mobile_presentation\UnifiedExperienceDesign_BookChapterfinal.pdf')
# Extract first 8 pages specifically
for i in range(min(8, len(reader.pages))):
    text = reader.pages[i].extract_text()
    if text:
        print(f'=== PAGE {i+1} ===')
        print(text)
        print()
