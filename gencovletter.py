""""
Need to read file from the input source : cover_letter.txt , skills.csv
cover_letter.txt : the format of your cover letter. Variables in the cover letter are #website , #inserttools , #toolproficient , #toolproficientyr , #company
skills.csv : it contains the skills you want to add for the given variables in the apt column
Find and replace the right variables
Create PDF with CoverLetter-companyName.pdf
need to install fpdf module for your python version
"""

from sys import argv
from fpdf import FPDF
import json
import csv


def write_cover_letter(cover_letter, skills):

    # open csv file and read input
    with open(skills) as skills_csv:

        reader = csv.reader(skills_csv)
        rownum = 0

        for row in reader:

            pdf = FPDF('P', 'mm', 'A4')  # portrait mode, mm , A4 size paper
            pdf.add_page()  # new blank page
            pdf.set_font('Arial', '', 12)  # font, Style (B,U,I) , fontsize in pt.

            #ignore the header row
            if rownum == 0:
                pass

            else:
                model_cover_letter = open(cover_letter, 'r')

                for line in model_cover_letter:

                    line = line.replace('#website', row[0])
                    line = line.replace('#inserttools', ','.join(row[1].split('#')))  # skills are seperated by '#' split and join them
                    line = line.replace('#toolproficient', row[2])
                    line = line.replace('#toolyr', row[3])
                    line = line.replace('#company', row[4])

                    pdf.write(6, line)

                pdf.output('cover_letters/Cover Letter - ' + row[4] + '.pdf', 'F')
                pdf.close()

            rownum = rownum + 1

if __name__ == "__main__":

    coverletter = argv[1]
    skillset = argv[2]

    # just use the right file names or modify the ones provided
    write_cover_letter(coverletter, skillset)
