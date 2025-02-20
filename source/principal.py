# principal.py
import tkinter as tk
from mesas import tela_mesas
from cardapio import tela_cardapio
from pedidos import tela_pedidos
from relatorios import tela_relatorios

def tela_principal():
    janela = tk.Tk()
    janela.title("Tela Principal")

    tk.Label(janela, text="Bem-vindo ao Sistema de Gestão de Restaurante!").pack(pady=20)

    # Botões para outras funcionalidades
    tk.Button(janela, text="Gerenciar Mesas", command=tela_mesas).pack(pady=10)
    tk.Button(janela, text="Gerenciar Cardápio", command=tela_cardapio).pack(pady=10)
    tk.Button(janela, text="Gerenciar Pedidos", command=tela_pedidos).pack(pady=10)
    tk.Button(janela, text="Gerar Relatórios", command=tela_relatorios).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    tela_principal()