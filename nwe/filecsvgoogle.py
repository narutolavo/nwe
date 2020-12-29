from googletrans import Translator
translator = Translator()
import csv

class Criarpdf:
	def __init__(self):				
		self.bd = []
		self.bdni = []
		self.bdsan = []
		with open('palavras02.csv', 'r') as self.arquivo_csv:
		    self.leitor = csv.DictReader(self.arquivo_csv, delimiter=',')
		    for coluna in self.leitor:
		        self.bd.append(coluna['listaingles'])
		        self.bdni.append(coluna['furigana;kanji'])

		for x in self.bd:
			try:
				self.item = str(x)	
				self.traduzi = translator.translate(self.item, dest='pt')
				self.traduzir = str(self.traduzi.text)
				self.controlando = self.traduzir
				self.bdsan.append(self.controlando)
			except TypeError:
				#print("'NoneType' object is not iterable") As traduções variam de acordo com o gênero das palavras
				self.controlando = self.item + "(As traduções variam)"
				self.bdsan.append(self.controlando)



		self.tamanhobdsan = len(self.bdsan)#a
		self.tamanhobdni = len(self.bdni)#b
		self.indice = 0 #pega os item da lista
		with open('palavraspdf.csv', 'w') as self.arquivo_csv:
			self.colunas = ['listaportugues', 'furigana;kanji']    
			self.escrever = csv.DictWriter(self.arquivo_csv, fieldnames=self.colunas, delimiter=',', lineterminator='\n')
			self.escrever.writeheader()	 
			for x in self.bdsan: #vai pecorrer a lista 'bdsan' 
				self.letraa = str(x)
				if self.indice < self.tamanhobdni: #para ir adicionando a lista 'bdni' eu crio uma variavel 'indice' de valor igual a 0, e aumento ela em 1, quando chegar a um valor em que for igual a lista 'b' ela para e vai para o 'else'
					self.item = self.bdni[self.indice]
					self.itemm = str(self.item)
					self.escrever.writerow({'listaportugues': self.letraa, 'furigana;kanji': self.itemm})
					self.indice += 1
				else:
					self.itemm = 'não tem item'
					self.escrever.writerow({'listaportugues': self.letraa, 'furigana;kanji': self.itemm})
					self.indice += 1

#Criarpdf()