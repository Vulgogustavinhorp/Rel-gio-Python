from tkinter import *
import datetime

# Cores
cor_fundo = "#000000"  # Preto
cor_texto = "#eb463b"  # Vermelho

# Função para atualizar o relógio
def atualizar_hora():
    agora = datetime.datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    data_atual = agora.strftime("%d/%m/%Y")
    label_hora.config(text=hora_atual)
    label_data.config(text=data_atual)
    # Atualiza a cada 1 segundo
    janela.after(1000, atualizar_hora)

# Criando a janela
janela = Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(False, False)
janela.configure(bg=cor_fundo)

# Label para hora
label_hora = Label(janela, font=("Arial Rounded MT Bold", 40), fg=cor_texto, bg=cor_fundo)
label_hora.pack(pady=10)

# Label para data
label_data = Label(janela, font=("Arial Rounded MT Bold", 20), fg=cor_texto, bg=cor_fundo)
label_data.pack()

# Iniciar o relógio
atualizar_hora()

janela.mainloop()