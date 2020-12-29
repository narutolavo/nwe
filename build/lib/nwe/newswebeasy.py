import requests
from bs4 import BeautifulSoup
import json

class News:
	def __init__(self, url):
		self.urls = url
		self.resp = requests.get(self.urls)
		self.resp.encoding = "UTF-8"

		self.soup = BeautifulSoup(self.resp.text, 'html.parser')

		self.titulo = self.soup.find(class_='article-main__title')
		self.textocorpo = self.soup.find(class_='article-main__body article-body')

		self.tituloo = self.titulo.prettify()
		self.textocorpoo = self.textocorpo.prettify()
		self.listano = self.tituloo + self.textocorpoo


		with open('titulocorpo_tags.json', 'w') as self.tbody:
		    self.tbody.write(str(self.listano))