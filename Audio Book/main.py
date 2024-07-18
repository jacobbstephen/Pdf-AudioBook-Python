# 1. Import packages
#2. speaker say
#3. get pdf file and read file
# to read python file=> PyPDF2

import pyttsx3
import PyPDF2
book = open('IP1.pdf', 'rb')
#used to read a book
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
speaker = pyttsx3.init() #create a speaker
for num in range(2, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()