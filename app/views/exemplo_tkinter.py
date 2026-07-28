import tkinter as tk  #tkinter é a biblioteca nativa do python pra interface gráfica
from tkinter import messagebox

janela = tk.Tk()

janela.title("Meu primeiro sisteminha")
janela.geometry("800x600")
janela.resizable(False, False) #pode modificar o tamanho da janela

lbl_titulo = tk.Label(
    janela,
    text = "EXEMPLO DE CADASTRO",
    font = ("Arial", 12, "bold")
)
lbl_titulo.grid(
    row = 0,
    column = 0,
    padx = 10,
    pady = 5,
    columnspan = 2,
    sticky = "e"
    # "w", "N", "E", "S" São os pontos cardiais pra definir a posiçao do titulo
)

lbl_nome = tk.Label( 
    janela, #onde o label vai abrir
    text = "Nome:"
)
lbl_nome.grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)

txt_nome = tk.Entry(
    janela, 
    width = 40   #+/- 40cracters de largura
)
txt_nome.grid(
    row = 1,
    column = 1
)

lbl_idade = tk.Label( 
    janela,
    text = "Idade:"
)
lbl_idade.grid(
    row = 2,
    column = 0,
    padx = 10,
    pady = 5
)
txt_idade = tk.Entry(
    janela,
    width = 40
)
txt_idade.grid(
    row = 2,
    column = 1
)
def printar():
    print(txt_nome.get())

#bnt de Botão
btn_escrever_nome = tk.Button(
    janela,
    text = "Printar o nome",
    command = printar
)

btn_escrever_nome.grid(
    row = 3,
    column = 0,
    padx = 10,
    pady = 5
)
def avaliar_idade():
    if txt_idade.get() == "":
        messagebox.showerror( #Icone vermelho de erro
            "Sisteminha",
            "Tu só pode estar de sacanagem!"
        )
        return    
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo( #Icone de quando deu certo
            "Sisteminha",
            "Com " + str(idade) + " você é bem vindo"
        )
        return
    messagebox.showwarning( #Icone de atençao
        "Sisteminha",
        "Menor de idade !!!!"
    )
    return
    
btn_avaliar_idade = tk.Button(
    janela,
    text = "Avaliar idade",
    command = avaliar_idade
)
btn_avaliar_idade.grid(
    row = 3,
    column = 1
)

janela.mainloop() #o que faz o codigo rodar