import csv

class Crianki:
	def __init__(self):
		self.bd = []
		self.bdni = []
		self.bdsan = []
		self.bdyon = {}
		with open('palavraspdf.csv', 'r') as self.arquivo_csv:
			self.leitor = csv.DictReader(self.arquivo_csv, delimiter=',')
			for coluna in self.leitor:
				self.bd.append(coluna['listaportugues'])
				self.bdni.append(coluna['furigana;kanji'])

		self.tamanhobd = len(self.bd)
		self.tamanhobdni = len(self.bdni)
		for x in range(1,self.tamanhobdni):
			self.bdyon[self.bdni[x]] = self.bd[x]


		'''for kanji,portugues in self.bdyon.items():
			self.bdsan.append('{} : {}'.format(kanji,portugues))'''

		with open('anki.txt', 'w') as self.arquivo_csv:
			self.colunas = ['furiganakanji', 'listaportugues']    
			self.escrever = csv.DictWriter(self.arquivo_csv, fieldnames=self.colunas, delimiter=',', lineterminator='\n')
			self.escrever.writeheader()

			for kanji,portugues in self.bdyon.items():
				self.escrever.writerow({'furiganakanji': kanji, 'listaportugues': portugues})

#Crianki()