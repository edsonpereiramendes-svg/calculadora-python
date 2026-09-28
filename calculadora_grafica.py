

import tkinter as tk

def clicar(valor):
    if valor == "=":
        try:
            resultado = str(eval(visor.get()))
            visor.set(resultado)
        except Exception:
            visor.set("Erro")
    elif valor == "C":
        visor.set("")
    elif valor == "sair":
        janela.destroy()
    
    else:
        visor.set(visor.get() + valor)

janela = tk.Tk()
janela.title("Minha Calculadora")

visor = tk.StringVar()
entrada = tk.Entry(janela, textvariable=visor, font=("Arial", 20), justify="right", width=20)
entrada.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

botoes = [
    "7", "8", "9", "/", "**",
    "4", "5", "6", "*", "%",
    "1", "2", "3", "-", "//",
    "C", "0", "=", "+", "sair",
]

for i, texto in enumerate(botoes):
    botao = tk.Button(janela, text=texto, width=4, height=2, bg="orange", fg="black",
                      command=lambda t=texto: clicar(t))
    botao.grid(row=1 + i // 5, column=i % 5, padx=2, pady=2, sticky="nsew")

janela.mainloop()
