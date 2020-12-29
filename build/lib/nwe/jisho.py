import requests
from bs4 import BeautifulSoup
import json
import csv

#inicio: importando funções de arquivos locais
from nwe.muitoslinks import Plinks
from nwe.muitoslinks import Pespalavra
#final: importando funções de arquivos locais


class Jisho:
	def __init__(self):
		self.arquivo = open("pesquisanesemfuria.json", "r")
		self.linha = self.arquivo.readlines()
		
		self.pesquisa = ''
		for self.x in self.linha:
			self.pesquisa += self.x


		# Cria variavel para armazenar a URL do site a ser raspado 最後学校答え中学校外国人必要韓国語質問
		self.url = 'https://jisho.org/search/'+self.pesquisa
			
		
		# Executa a requisição ao site e armazena o retorno na variavel
		self.resp = requests.get(self.url)
		self.resp.encoding = "UTF-8" #trazer os caracteres japoneses sem erros

		self.soup = BeautifulSoup(self.resp.text, 'html.parser')
		

		self.mui_palavras = self.soup.find('section', id='zen_bar') #aqui ele vai procurar por essa tag section e id, ela só vai existe se for mandado mais de uma palavra para pesquisa no jisho



		if self.mui_palavras == None: #aqui vai verificar o resuldo do 'find' se tiver sido só uma palavra pesquisada, o resultado armazenado na variavel 'mui_palavras' vai ser 'None' ou seja não tem lista ai não vai procurar os outros links das palavras.
			self.resultado_list = self.soup.find(class_='concept_light-meanings medium-9 columns')
			self.resultado_furigana = self.soup.find(class_='concept_light-readings japanese japanese_gothic')#class="concept_light-wrapper columns zero-paddingconcept_light-readings japanese japanese_gothic"
			self.pesump = Pespalavra()
			self.a = self.pesump.pespalavra(self.resultado_list)
			self.b = self.pesump.kanjifuri(self.resultado_furigana)
			
			self.tamanhoa = len(self.a)
			self.tamanhob = len(self.b)
			self.indice = 0 #pega os item da lista
			with open('palavras01.csv', 'w') as self.arquivo_csv:
			    self.colunas = ['listaingles', 'furigana;kanji']    
			    self.escrever = csv.DictWriter(self.arquivo_csv, fieldnames=self.colunas, delimiter=',', lineterminator='\n')
			    self.escrever.writeheader()	 
			    for self.x in self.a: #vai pecorrer a lista 'a' 
			    	self.letraa = str(self.x)
			    	if self.indice < self.tamanhob: #para ir adicionando a lista 'b' eu crio uma variavel 'indice' de valor igual a 0, e aumento ela em 1, quando chegar a um valor em que for igual a lista 'b' ela para e vai para o 'else'
			    		self.item = self.b[self.indice]
				    	self.itemm = str(self.item)
				    	self.escrever.writerow({'listaingles': self.letraa, 'furigana;kanji': self.itemm})
				    	self.indice =+ 1
			    	else:
			    		self.itemm = 'não tem item'
			    		self.escrever.writerow({'listaingles': self.letraa, 'furigana;kanji': self.itemm})
			    		self.indice =+ 1

		else:
			self.liste = self.mui_palavras.find_all('li', 'clearfix japanese_word')
			self.resultado_furigana = self.soup.find(class_='concept_light-readings japanese japanese_gothic')
			self.pesquisalinks = Plinks(self.liste)
			self.a = self.pesquisalinks.imprimilista()
			self.b = []
			for self.x in self.a:
				self.b.append(self.x)
			self.linkspala = self.pesquisalinks.gerapesquisa()
			self.pes = Pespalavra()
			self.s = self.pes.pesquisaVP(self.b)

			with open('palavras02.csv', 'w') as self.arquivo_csv:
			    self.colunas = ['listaingles', 'furigana;kanji']    
			    self.escrever = csv.DictWriter(self.arquivo_csv, fieldnames=self.colunas, delimiter=',', lineterminator='\n')
			    self.escrever.writeheader()
			    self.indice = 0
			    self.itemm = 'itemm vazio'
			    self.letraa ='letraa vazio'
			    for self.x in self.s: #vai pecorrer a lista 'a' 
			    	if self.indice % 2 == 0:
			    		self.itemm = ''
			    		for self.l in self.x:
			    			self.itemm += self.l+' ' #separar o kanji e o furigana na hora de salvar na coluna do arquivo csv
			    		self.itemm = self.itemm[:-1] #exclui o ultimo " "
			    		
			    		self.escrever.writerow({'listaingles': self.letraa, 'furigana;kanji': self.itemm})	
			    		self.indice += 1
			    	else:
			    		self.letraa = self.x[0]
			    		self.indice += 1