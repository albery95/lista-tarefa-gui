#!/usr/bin/env python3
#
#  teste.py
#  
#  Copyright 2026 albery <albery@albery-notebook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import tkinter as tk
from tkinter import messagebox
import os
import json

ARQUIVO_TAREFAS = "tarefas_gui.json"

class GerenciadorTarefas:
	def __init__(self, root):
		self.root = root
		self.root.title("Meu Gerenciador de Tarefas")
		self.root.geometry("400x450")
		
		self.tarefas = self.carregar_tarefas()
		
		# ---Elementos da Interface---
		self.label = tk.Label(root, text="O que precisa ser feito?", font=("Arial",12))
		self.label.pack(pady=10)
		
		self.entrada_tarefa = tk.Entry(root, font=("Arial", 12), width=30)
		self.entrada_tarefa.pack(pady=5)
		# Permite adicionar apertando enter
		self.entrada_tarefa.bind('<Return>', lambda event: self.adicionar_tarefa())
		self.btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa, bg="#4CAF50", fg="white")
		self.btn_adicionar.pack(pady=5)
		
		self.lista_tarefas = tk.Listbox(root, font=("Arial",12), width=40, height=10)
		self.lista_tarefas.pack(pady=10, padx=10)
		
		self.btn_remover = tk.Button(root, text="Remover Selecionada", command=self.remover_tarefa, bg="#f44336", fg="white")
		self.btn_remover.pack(pady=5)
		
		#Atualiza a lista visual logo ao abrir
		self.atualizar_listbox()

	def carregar_tarefas(self):
		# Verifica se o arquivo existe antes de tentar abrir
		if os.path.exists(ARQUIVO_TAREFAS):
			with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
				return json.load(f)
		return []
	def salvar_tarefas(self):
		with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
			json.dump(self.tarefas, f, indent=4, ensure_ascii=False)

	def adicionar_tarefa(self):
		tarefa = self.entrada_tarefa.get()
		if tarefa != "":
			self.tarefas.append(tarefa)
			self.atualizar_listbox()
			self.salvar_tarefas()
			self.entrada_tarefa.delete(0, tk.END)
		else:
			messagebox.showwarning("Aviso", "Digite alguma tarefa!")

	def remover_tarefa(self):
		try:
			indice = self.lista_tarefas.curselection()[0]
			self.tarefas.pop(indice)
			self.atualizar_listbox()
			self.salvar_tarefas()
		except IndexError:
			messagebox.showwarning("Aviso", "Selecione uma tarefa para remover")

	def atualizar_listbox(self):
		self.lista_tarefas.delete(0, tk.END)
		for tarefa in self.tarefas:
			self.lista_tarefas.insert(tk.END, tarefa)
	

if __name__ == "__main__":
	root = tk.Tk()
	app = GerenciadorTarefas(root)
	root.mainloop()



