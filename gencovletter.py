""""
Use notepad++ to save the txt file as ISO-8859-1 encoding
"""

from fpdf import FPDF
from ftfy import fix_text
import time
import os

def write_cover_letter(customization):
    pdf = FPDF('P', 'mm', 'Letter')  # portrait mode, mm , A4 size paper
    pdf.add_page()  # new blank page
    pdf.set_font('Times', '', 12)  # font, Style (B,U,I) , fontsize in pt.

    model_cover_letter = open("cover_letter.txt", 'r', encoding="ISO-8859-1")

    for line in model_cover_letter:
        line = fix_text(line)
        
        for key, value in customization.items():
            full_variable_name = "#" + key
            line = line.replace(full_variable_name, value)

        pdf.write(6, line) #6 is line height

    file_name = customization["file_name"]

    try:
        pdf.output(file_name + '.pdf', 'F')
    except:
        os.system("taskkill /im Acrobat.exe")
        time.sleep(1)
        pdf.output(file_name + '.pdf', 'F')

    pdf.close()

if __name__ == "__main__":
    customization = {
    "file_name": 'Yi_(Zack)_Zhang_Cover_Letter',
    "company": "Google",
    # "field": "software engineering",
    "field": "data science",
    # "internship": "Software Engineer Internship",
    "internship": "Research Internship",
    "period": "the summer of 2020",
    "skills": "natural language processing",
    }

    write_cover_letter(customization)
    os.system("start " + customization["file_name"] + '.pdf')
