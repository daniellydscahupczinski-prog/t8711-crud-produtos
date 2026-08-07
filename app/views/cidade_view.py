from app.models.cidade import Cidade

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Cidade_view:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller 
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Cidade")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Cidade"
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados da cidade"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column = 1,
            padx = 5,
            sticky = "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = "Nome:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_estado = tk.Label(
            self.frm_dados,
            text = "Estado:"
        )
        self.lbl_estado.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_estado = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_estado.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnpan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_cidade = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_cidade.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_cidade["columns"] = (
            "id",
            "nome",
            "estado"
        )
        self.tbl_cidade.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_cidade.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_cidade.column(
            "nome",
            width = 50
        )
        self.tbl_cidade.column(
            "estado",
            width = 20
        )
        self.tbl_cidade.heading(
            "id",
            text = "ID"
        )
        self.tbl_cidade.heading(
            "nome",
            text = "Nome"
        
        )
        self.tbl_cidade.heading(
            "estado",
            text = "Estado"
        )

    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_cidade.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cidade
        )
    
    def carregar_estado(self, estado):
        self._estado = estado
        valores = []
        for estado in estado:
            valores.append(
                f"{estado.id} - {estado.nome}"
            )
        self.cmb_estado["values"] = valores
        self.cmb_estado.set("")
        
    def preencher_campos (self, cidade):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(cidade.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            cidade.nome
        )
        self.txt_estado.insert(
            0,
            cidade.estado
        )

        for indice, estado in enumerate(self._estado):
            if estado.id == cidade.estado.id:
                self.cmb_estado.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.cmb_estado.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_cidade.get_children():
            self.tbl_cidade.delete(item)

    def get_id_selecionado(self):

        item = self.tbl_cidade.selection()[0]

        return self.tbl_cidade.item(item)["values"][0]
    
    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir essa cidade?"
        )
    
    def ler_dados_cidade(self):
        nome = self.txt_nome.get()
        indice = self.cmb_estado.current()
        if indice < 0:
            raise ValueError("Selecione um Estado.")
        estado = self._estado[indice]
        return nome, estado
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem
            )
    def exibir_cidade(self, cidade):
        self.limpar_treeview()

        for cidade in cidade:
            self.tbl_cidade.insert(
                "",
                tk.END,
                values=(
                    cidade.id,
                    cidade.nome,
                    cidade.estado
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_estado()
        self.controller.get_all()
        self.root.mainloop()
