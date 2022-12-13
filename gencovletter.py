""""
Use notepad++ to save the txt file as ISO-8859-1 encoding
"""

from fpdf import FPDF
from ftfy import fix_text
import time
import os

line_height = 6

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

        if "https:" not in line:
            pdf.write(line_height, line)  # 6 is line height
        else:
            link_idx = line.find("https:")
            before_link = line[:link_idx]
            after_link = line[link_idx:].strip()
            pdf.write(line_height, before_link)
            pdf.set_text_color(0, 0, 255)
            pdf.set_font('', 'U')
            pdf.write(line_height, line[link_idx:], link=after_link)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('', '')

    file_name = customization["file_name"]

    # windows
    # try:
    #     pdf.output(file_name + '.pdf', 'F')
    # except:
    #     os.system("taskkill /im Acrobat.exe")
    #     time.sleep(1)
    #     pdf.output(file_name + '.pdf', 'F')

    os.system("killall -KILL AdobeAcrobat")  # for mac
    time.sleep(1)
    pdf.output(file_name + '.pdf', 'F')

    pdf.close()


if __name__ == "__main__":
    customization = {
        "file_name": 'Zack_Light_Cover_Letter',
        "company": "DRW",
        "position": "the Trading Systems Engineer (Algo) position",
        # "field": "software engineering",
        # "field": "data science",
        # "period": "the summer of 2020",
        # "skills": "natural language processing",
    }

    write_cover_letter(customization)
    os.system("open " + customization["file_name"] + '.pdf')
