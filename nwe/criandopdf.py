from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import ParagraphStyle as PS

#from reportlab.lib.pagesizes import A4
import csv

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

class Umupdf:
	def __init__(self, link):
		self.url = link
		self.link = "<a href='"+self.url+"' color='blue'>News Web Easy</a>"
		self.bd = []
		self.bdni = []
		self.bdsan = []
		self.bdyon = {}
		self.elementos = []
		self.fonte = PS(name='fonte1', fontSize=14, fontName='HeiseiMin-W3', spaceBefore=8, spaceAfter=8, leading=16)
		with open('newsartigo.txt', 'r') as self.arquivo_txt:
			self.artigo = self.arquivo_txt.readlines()
		
		self.elementos.append(Paragraph(self.link, self.fonte))
		for line in self.artigo:
			self.elementos.append(Paragraph(line, self.fonte))

		with open('palavraspdf.csv', 'r') as self.arquivo_csv:
			self.leitor = csv.DictReader(self.arquivo_csv, delimiter=',')
			for coluna in self.leitor:
				self.bd.append(coluna['listaportugues'])
				self.bdni.append(coluna['furigana;kanji'])
		self.tamanhobd = len(self.bd)
		self.tamanhobdni = len(self.bdni)
		self.valor = 1
		#print(self.tamanhobdni)
		for x in range(1,self.tamanhobdni):
			self.bdyon[self.bdni[x]] = self.bd[x]
			
		self.estilo = getSampleStyleSheet()

		for kanji,portugues in self.bdyon.items():
			self.elementos.append(Paragraph('{} : {}'.format(kanji,portugues), self.fonte))
	   
		self.docpdf = SimpleDocTemplate("nwe.pdf", pagesize=letter, title='nwe', author='narutoolavo')
		self.docpdf.build(self.elementos)

		self.fedit = ''
		self.fedit += self.link
		self.fedit += '\n'
		for x in self.artigo:
			self.fedit += x
		self.fedit += '\n'

		for kanji,portugues in self.bdyon.items():
			self.fedit += '{} : {} \n'.format(kanji,portugues)
		with open("nwe_editar.txt", "w") as self.fileedit:
			self.fileedit.write(str(self.fedit))


#Umupdf()
