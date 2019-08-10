""""
Use notepad++ to save the txt file as ISO-8859-1 encoding
"""

from fpdf import FPDF
from ftfy import fix_text
import time
import os

def write_cover_letter(company, field, internship, period, fn):
    pdf = FPDF('P', 'mm', 'Letter')  # portrait mode, mm , A4 size paper
    pdf.add_page()  # new blank page
    pdf.set_font('Times', '', 12)  # font, Style (B,U,I) , fontsize in pt.

    model_cover_letter = open("cover_letter.txt", 'r', encoding="ISO-8859-1")

    for line in model_cover_letter:
        line = fix_text(line)

        line = line.replace('#company', company)
        line = line.replace('#internship', internship)
        line = line.replace('#period', period)
        line = line.replace('#field', field)

        pdf.write(6, line) #6 is line height

    try:
        pdf.output(fn + '.pdf', 'F')
    except:
        os.system("taskkill /im Acrobat.exe")
        time.sleep(1)
        pdf.output(fn + '.pdf', 'F')

    pdf.close()

if __name__ == "__main__":
    company = "Boston Road Runners"
    field = "data science"
    internship = "Data Analytics Internship"
    period = "the next year"
    fn = 'Yi_(Zack)_Zhang_Cover_Letter'
    write_cover_letter(company, field, internship, period, fn)
    os.system("start " + fn + '.pdf')
