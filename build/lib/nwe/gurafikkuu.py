import tkinter as tk
from tkinter import ttk
#pacotes nwe
from nwe.newswebeasy import News
from nwe.usandore import Usarre
from nwe.jisho import Jisho
from nwe.filecsvgoogle import Criarpdf
from nwe.criandopdf import Umupdf
from nwe.criaanki import Crianki

class Tela:

	def __init__(self, master):

		self.nossatela = master

		#self.coisa = tk.nomdedowidget(widgetpai. opçoesdeconfiguraçao)
		self.nossatela.title("nwe")
		self.nossatela.geometry("500x200+200+100")

		#self.nossatela.wm_iconbitmap("@ne.xbm") 

		self.frame = tk.Frame(self.nossatela)
		self.frame.pack()

		self.frame2 = tk.Frame(self.nossatela)
		self.frame2.pack()

		self.frame3 = tk.Frame(self.nossatela)
		self.frame3.pack()

		self.frame4 = tk.Frame(self.nossatela)
		self.frame4.pack()

		self.texto = tk.Label(self.frame2, text="Insira o link: ")
		self.texto.pack(side=tk.LEFT, pady=10)


		self.entrada = tk.Entry(self.frame2)
		self.entrada.pack(side=tk.LEFT, pady=10, padx=10)
		

		self.botao = tk.Button(self.frame2, text="Iniciar", font=("Verdana", "14"), command=self.respostabotao)
		self.botao.pack()

		self.botao2 = tk.Button(self.frame4, text="Gerar PDF", font=("Verdana", "14"), command=self.gerarpdf)
		self.botao2.pack()

		self.botao3 = tk.Button(self.frame4, text="Criar Anki", font=("Verdana", "14"), command=self.cardanki)
		self.botao3.pack()

		self.barradeprogresso = ttk.Progressbar(self.frame3, length=200)
		self.barradeprogresso.pack()		

		self.textoaguarde = tk.Label(self.frame3, text=" ")
		self.textoaguarde.pack()

		self.label = tk.Label(self.frame, text="NWE", font=("Verdana", "20"))
		self.label.pack()

	def upbarraprogresso(self, valor):
		self.valore = valor
		self.barradeprogresso["value"] = self.valore
		self.barradeprogresso["maximum"] = 4
		self.barradeprogresso.update()
		if self.barradeprogresso["value"] == 4:
			self.textoaguarde["text"] = "Você já pode gerar o Pdf"


	def respostabotao(self):
		self.textoaguarde["text"] = "Aguarde..."
		self.valor = 0

		self.link = self.entrada.get()
		News(self.link)
		self.valor += 1
		self.upbarraprogresso(self.valor)

		Usarre()
		self.valor += 1
		self.upbarraprogresso(self.valor)

		Jisho()
		self.valor += 1
		self.upbarraprogresso(self.valor)

		Criarpdf()
		self.valor += 1
		self.upbarraprogresso(self.valor)

	def gerarpdf(self):
		self.barradeprogresso.stop()
		Umupdf()
		self.textoaguarde["text"] = "Arquivo Pdf gerado..."

	def cardanki(self):
		Crianki()
		self.textoaguarde["text"] = "Cartão Anki gerado..."



#gerar a nossa interface
def main():
	Janelaraiz = tk.Tk()

	Tela(Janelaraiz)

	Janelaraiz.mainloop()


