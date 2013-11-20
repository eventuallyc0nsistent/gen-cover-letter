# Need to read file from the input source : cover_letter.txt , skills.txt
# Choose the variables from the variables list
# Find and replace the right variables (#website , #inserttools , #toolproficient , #toolproficientyr)
# Create PDF

from fpdf import FPDF
import json

class CoverLetter(object):
	
	def __init__(self,cover_letter,skills):

		self.cover_letter = open(cover_letter,'r')
		self.skills = open(skills)
		self.writePDF(self.cover_letter,self.skills)

	# read file and skills
	def writePDF(self,cover_letter,skills):

		self.pdf = FPDF('P','mm','A4') # portrait mode, mm , A4 size paper
		self.pdf.add_page()
		self.pdf.set_font('Arial','',12)
		self.skills = skills.readlines()
		

		for line in self.cover_letter:
			line = line.replace('#website',self.skills[1].rstrip('\n'))
			line = line.replace('#inserttools',self.skills[3].rstrip('\n'))
			line = line.replace('#toolproficient',self.skills[5].rstrip('\n'))
			line = line.replace('#toolyr',self.skills[7].rstrip('\n'))
			line = line.replace('#company',self.skills[9].rstrip('\n'))
			self.pdf.write(6,line)

		self.pdf.output(self.skills[9]+'.pdf','F')

CoverLetter('cover_letter.txt','skills.txt')
