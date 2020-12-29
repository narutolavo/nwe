import re

class Usarre:
	def __init__(self):
		self.arquivo = open("titulocorpo_tags.json", "r+t")
		self.texto = self.arquivo.readlines()

		self.modelandotags = ''
		for self.x in self.texto:
			self.modelandotags += self.x.strip('\n \t')


		self.hirafurikanji = re.findall(r'[\w\.]', self.modelandotags)
		self.pala = ''
		for self.x in self.hirafurikanji:
			self.pala += self.x

		self.sspan = re.findall(r'[^span]', self.pala)
		self.ssjunta = ''
		for self.x in self.sspan:
			self.ssjunta += self.x

		self.resupalaa= re.sub(r'[rubyrtspan W m l"href" "id0002" "javascript:void(0)" "id0001" "colorC" "colorL" "__" \s]','-', self.ssjunta) 

		self.resultadoka=re.findall(r'----(\w+)',self.resupalaa) 
	
		self.juntakhka = ''

		for self.x in self.resultadoka:
			self.juntakhka += self.x

		with open('pesquisanesemfuria.json', 'w') as self.semfuri:
		    self.semfuri.write(str(self.juntakhka))

		#cria arquivo para o artigo que vai ser gerado no criandopdf
		self.juntando = ''
		for self.x in self.resultadoka:
			self.juntando += self.x

		with open('newsartigo.txt', 'w') as self.sfuri:
		    self.sfuri.write(str(self.juntando))

#Usarre()
