# Need to read file from the input source : cover_letter.txt , skills.txt
# Choose the variables from the variables list
# Find and replace the right variables (#website , #inserttools , #toolproficient , #toolproficientyr)
# Create PDF

from fpdf import FPDF
import json
import csv

class CoverLetter(object):
	
	def __init__(self,cover_letter,skills):

		self.cover_letter = open(cover_letter,'r')
		self.skills = skills
		self.writePDF(self.cover_letter,self.skills)

	# read coverletter and skills csv
	def writePDF(self,cover_letter,skills):

		self.pdf = FPDF('P','mm','A4') # portrait mode, mm , A4 size paper
		self.pdf.add_page() # new page added
		self.pdf.set_font('Arial','',12) # font, Style (B,U,I) , fontsize in pt.
		
		# open csv file and read input
		with open(self.skills) as skills_csv:

			reader = csv.reader(skills_csv)
			rownum = 0

			for row in reader:
				
				#ignore the header row
				if rownum == 0:
					pass

				else :
					for line in self.cover_letter:

						line = line.replace('#website',row[0])
						line = line.replace('#inserttools',','.join(row[1].split('#'))) # skills are seperated by '#' split and join them
						line = line.replace('#toolproficient',row[2])
						line = line.replace('#toolyr',row[3]) 
						line = line.replace('#company',row[4])
						self.pdf.write(6,line)

					self.pdf.output('Cover Letter - '+row[4]+'.pdf','F')
				
				rownum = rownum + 1

				
# just use the right file names or modify the ones provided
CoverLetter('cover_letter.txt','skills.csv')
