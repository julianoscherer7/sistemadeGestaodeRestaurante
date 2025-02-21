import tkinter as tk
from tkinter.font import Font
from mesas import tela_mesas
from cardapio import tela_cardapio
from pedidos import tela_pedidos
from relatorios import tela_relatorios

def on_enter(event):
    """Função chamada quando o mouse entra no botão."""
    event.widget.config(bg="#2980B9")  # Muda a cor de fundo para um azul mais escuro

def on_leave(event):
    """Função chamada quando o mouse sai do botão."""
    event.widget.config(bg="#3498DB")  # Volta à cor de fundo original

def tela_principal():
    # Configuração da janela
    janela = tk.Tk()
    janela.title("Tela Principal")
    janela.geometry("1024x768")  # Resolução maior
    janela.configure(bg="#2C3E50")  # Fundo azul escuro moderno

    # Frame principal
    frame = tk.Frame(janela, bg="#2C3E50")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

    # Fonte moderna para o título
    fonte_titulo = Font(family="Helvetica", size=28, weight="bold")
    fonte_texto = Font(family="Helvetica", size=14)

    # Título
    titulo = tk.Label(frame, text="Sistema de Gestão de Restaurante", font=fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
    titulo.grid(row=0, column=0, columnspan=2, pady=40)

    # Botões para outras funcionalidades
    botoes = [
        ("Gerenciar Mesas", tela_mesas),
        ("Gerenciar Cardápio", tela_cardapio),
        ("Gerenciar Pedidos", tela_pedidos),
        ("Gerar Relatórios", tela_relatorios)
    ]

    for i, (texto, comando) in enumerate(botoes):
        botao = tk.Button(
            frame,
            text=texto,
            font=fonte_texto,
            bg="#3498DB",  # Azul mais claro
            fg="#FFFFFF",  # Texto branco
            activebackground="#2980B9",  # Azul mais escuro ao clicar
            activeforeground="#FFFFFF",
            relief="flat",  # Remove borda padrão
            bd=0,  # Remove borda
            padx=30,
            pady=15,
            command=comando,
            width=20  # Largura fixa para todos os botões
        )
        botao.grid(row=i + 1, column=0, columnspan=2, pady=10, sticky="ew")  # Alinha os botões horizontalmente

        # Adiciona efeito de hover
        botao.bind("<Enter>", on_enter)  # Quando o mouse entra no botão
        botao.bind("<Leave>", on_leave)  # Quando o mouse sai do botão

    # Configuração do grid para centralizar e alongar os botões
    frame.grid_columnconfigure(0, weight=1)  # Centraliza os botões
    frame.grid_columnconfigure(1, weight=1)  # Centraliza os botões

    janela.mainloop()

if __name__ == "__main__":
    tela_principal()