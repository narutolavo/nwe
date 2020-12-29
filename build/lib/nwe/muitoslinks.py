import requests
from bs4 import BeautifulSoup
"""Essa classe é para pegar uma lista gerada pela função find_all, com as tags 'li', ai depois procurar os links e tira os href para poder pesquisar as palavras.
ai gera um dicionario com as palavras para pesquisa elas"""
class Plinks:
	"""docstring for ClassName"""

	def __init__(self, value = []):
		self.liste2 = []
		self.juntar(value)
		self.listalink = []
		for self.x in self.liste2: #pega os links das pesquisas
			self.y = self.x.find_all('a') #aqui vai lá e pega todas as tags 'a' que no caso é só uma
			for self.x in self.y: #aqui vou anda na lista gerada pelo 'find_all'
				self.armazena = self.x['href']
				self.listalink.append(self.armazena)
		self.a = self.listalink
		#return self.listalink

	def imprimilista(self):
		return (self.a)

	def gerapesquisa(self): #aqui pega so os links
		self.item = 'link'
		self.valores = '0'
		self.listaaa = []
		self.dicio = {}
		while self.listalink:
			self.valor = len(self.listalink) #pega o tamanho da lista
			self.valores = str(self.valor) #aqui pego o tamanho da lista por exemplo 4, coverto par 'string' e armazeno em valores
			self.criav = self.item+self.valores #aqui eu junto o nome 'link' armazenado na variavel 'item' para criar uma variavel tipo 'link4'
			self.veiodlis = self.listalink.pop(0) #aqui eu pego o primeiro item da lista e armazeno na variavel 'veiodlis'
			self.dicio [self.criav] = self.veiodlis #aqui eu junto tudo, crio o dicionario com o 'link4' e o link da lista
			self.listaaa.append(self.criav) #aqui vou adicionando os 'link@(numeros), link4'

	def gerandol(self):
		return listaaa

	def juntar(self, value): #ao criar a liste2 vazia que é para alocar os links tem que juntar eles nela.
		for x in value:
			if not x in self.liste2:
				self.liste2.append(x)

class Pespalavra:
			
			def pespalavra(self, resultado_list):
				
				self.colocarf_csv = [] #pra colocar as palavras da tradução do jisho
				self.resultado_listi = resultado_list
				self.numerodeclass = self.resultado_listi.find_all(class_='meaning-meaning') #pega todas as traduçoes em ingles que o dicionario gera
				self.numerodetraduçao = len(self.numerodeclass) #pega o numero de traduçao

				self.lii = 0
				while self.lii < self.numerodetraduçao: 
					self.uma_p = self.numerodeclass[self.lii].get_text()
					
					self.colocarf_csv.append(self.uma_p)
					self.lii = self.lii + 1
				return self.colocarf_csv
				
			def kanjifuri(self, resultado_furigana): #aqui vai pegar a leitura(furigana) e a palavra em kanji
				self.resultado_furi = resultado_furigana
				self.lista_a_csv = []
				self.lista_r_space = []
				self.furigana = self.resultado_furi.find(class_='furigana')
				self.textkanji = self.resultado_furi.find(class_='text')
				self.botalista0 = self.furigana.get_text()
				self.botalista1 = self.textkanji.get_text()

				self.botalista4 = self.botalista0.split('\n') + self.botalista1.split('\n')
				self.botalista5 = self.botalista0.split('\n')

				self.botalista = self.furigana.get_text('\n') + self.textkanji.get_text('\n')
				
				self.listasemespaco = []
				for x in self.botalista4:
					self.listasemespaco.append(x.strip('\n \t'))
				self.listasemspace = []
				
				self.lspace = 0
				for x in self.listasemespaco:
					if x == '' or x == '      ':
						self.lspace += 1
						#print("vazio")
					else:
						self.listasemspace.append(x)
				return self.listasemspace
			def pesquisaVP(self, value = []):
				self.listaregula = ['n', 'a', 'r', 'u', 't', 'o' ]
				self.matrizes = [] #vai armazenar todas as listas da da função 'pespalavra e kanjifuri' que vem da soups para poder retorna para criar os arquivos csv
				self.matrizes.append(self.listaregula)
				self.listamarzena = []
				self.lista_li_recebida = [] #cria a lista responsavel por armazena os links
				self.junta(value) #aqui chama a função 'juntar' que pega a lista que vem e passa para a lista 'lista_li_recebida'

				for self.links in self.lista_li_recebida: #aqui vai pega cada link para pesquisa na url
					self.url = 'https://jisho.org'+self.links
					self.soupPes(self.url)
				return self.matrizes

			def soupPes(self, url): #aqui vai pesquisa a url
				self.resp = requests.get(url)
				self.resp.encoding = "UTF-8" #trazer os caracteres japoneses sem erros
				self.soup = BeautifulSoup(self.resp.text, 'html.parser')
				self.resultado_list = self.soup.find(class_='concept_light-meanings medium-9 columns')
				self.resultado_furigana = self.soup.find(class_='concept_light-readings japanese japanese_gothic')
				
				self.nenhumap = 0
				if self.resultado_list == None: #se não ouver uma palavra correspondente no jisho, o 'find' pode vim sem resultado o 'None'.
					#print("Não foi possível encontrar nenhuma palavra correspondente")
					self.nenhumap += 1
				else:
					self.listasoup = self.pespalavra(self.resultado_list) #chama a principal para retorna apenas a lista de palavras
					self.matrizes.append(self.listasoup)
					self.listakan = self.kanjifuri(self.resultado_furigana)
					self.matrizes.append(self.listakan)

			def junta(self, value): #ao criar a liste2 vazia que é para alocar os links tem que juntar eles nela.
				for x in value:
					
					if not x in self.lista_li_recebida:
						self.lista_li_recebida.append(x)
										
										
