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
    def __init__(self):
        self.bd = []
        self.bdni = []
        self.bdsan = []
        self.bdyon = {}
        self.elementos = []
        self.fonte = PS(name='fonte1', fontSize=14, fontName='HeiseiMin-W3', spaceBefore=8, spaceAfter=8, leading=16)
        with open('newsartigo.txt', 'r') as self.arquivo_txt:
            self.artigo = self.arquivo_txt.readlines()
        #print(self.artigo)
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
        
        #self.fonte = PS(name='fonte1', fontSize=14, fontName='HeiseiMin-W3', spaceBefore=8)
        self.estilo = getSampleStyleSheet()
        #self.elementos = []

        for kanji,portugues in self.bdyon.items():
            self.elementos.append(Paragraph('{} : {}'.format(kanji,portugues), self.fonte))
       
        self.docpdf = SimpleDocTemplate("nwe.pdf", pagesize=letter, title='GifuNI', author='narutoolavo')
        self.docpdf.build(self.elementos)


#Umupdf()