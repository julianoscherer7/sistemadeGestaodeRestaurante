import tkinter as tk
from tkinter import ttk
from database import conectar

def listar_itens():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Itens")
        itens = cursor.fetchall()
        conexao.close()
        return itens
    return []

def tela_cardapio(parent, callback_principal):
    janela = tk.Toplevel(parent)
    janela.title("Cardápio")
    janela.geometry("600x400")
    janela.configure(bg="#2C3E50")

    # Frame principal
    frame = ttk.Frame(janela, padding="10")
    frame.pack(pady=10)

    # Título
    ttk.Label(frame, text="Cardápio", font=("Helvetica", 18, "bold"), background="#2C3E50", foreground="#ECF0F1").pack(pady=10)

    # Lista de itens
    itens = listar_itens()
    for i, item in enumerate(itens):
        ttk.Label(frame, text=f"{item[1]} - R${item[3]:.2f}", background="#2C3E50", foreground="#ECF0F1").pack()

    # Botão para voltar à tela principal
    ttk.Button(
        frame,
        text="Voltar",
        command=lambda: [janela.destroy(), callback_principal()],
        style='TButton'
    ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    tela_cardapio(root, lambda: None)
    root.mainloop()