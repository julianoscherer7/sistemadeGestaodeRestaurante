import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar

def criar_pedido(id_mesa, itens_selecionados, valor_total):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Inserir o pedido na tabela Pedidos
            cursor.execute("INSERT INTO Pedidos (ID_Mesa, Preco_Total) VALUES (%s, %s)", (id_mesa, valor_total))
            id_pedido = cursor.lastrowid  # Pegar o ID do pedido criado

            # Inserir os itens do pedido na tabela Itens_Pedido
            for item in itens_selecionados:
                cursor.execute("INSERT INTO Itens_Pedido (ID_Pedido, ID_Item, Quantidade) VALUES (%s, %s, %s)",
                              (id_pedido, item['id'], item['quantidade']))

            # Atualizar o status da mesa para "Ocupada"
            cursor.execute("UPDATE Mesas SET Status = 'Ocupada' WHERE ID = %s", (id_mesa,))

            conexao.commit()
            messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pedido: {e}")
        finally:
            conexao.close()
    else:
        messagebox.showerror("Erro", "Falha ao conectar ao banco de dados.")

def carregar_itens():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT ID, Nome, Preco FROM Itens")
            itens = cursor.fetchall()
            return itens
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar itens: {e}")
            return []
        finally:
            conexao.close()
    else:
        messagebox.showerror("Erro", "Falha ao conectar ao banco de dados.")
        return []

def tela_pedidos(janela_principal, callback_voltar):
    janela = tk.Toplevel(janela_principal)
    janela.title("Pedidos")
    janela.geometry("800x600")
    janela.configure(bg="#2C3E50")

    # Frame para o número da mesa
    frame_mesa = ttk.Frame(janela, padding="10")
    frame_mesa.pack(pady=10)

    ttk.Label(frame_mesa, text="Número da Mesa:", background="#2C3E50", foreground="#ECF0F1").grid(row=0, column=0, padx=5, pady=5)
    entry_mesa = ttk.Entry(frame_mesa)
    entry_mesa.grid(row=0, column=1, padx=5, pady=5)

    # Frame para a lista de itens
    frame_itens = ttk.Frame(janela, padding="10")
    frame_itens.pack(pady=10)

    ttk.Label(frame_itens, text="Selecione os Itens:", background="#2C3E50", foreground="#ECF0F1").pack()

    # Lista de itens com Checkbuttons
    itens = carregar_itens()
    itens_selecionados = []

    for item in itens:
        item_frame = ttk.Frame(frame_itens)
        item_frame.pack(fill="x", pady=2)

        var = tk.IntVar()
        quantidade = tk.IntVar(value=1)

        ttk.Checkbutton(item_frame, text=f"{item[1]} - R${item[2]:.2f}", variable=var, style='TCheckbutton').pack(side="left", padx=5)
        ttk.Spinbox(item_frame, from_=1, to=10, textvariable=quantidade, width=5).pack(side="left", padx=5)

        itens_selecionados.append({
            'id': item[0],
            'nome': item[1],
            'preco': item[2],
            'var': var,
            'quantidade': quantidade
        })

    # Frame para o valor total
    frame_total = ttk.Frame(janela, padding="10")
    frame_total.pack(pady=10)

    ttk.Label(frame_total, text="Valor Total:", background="#2C3E50", foreground="#ECF0F1").pack(side="left", padx=5)
    label_total = ttk.Label(frame_total, text="R$ 0.00", background="#2C3E50", foreground="#ECF0F1")
    label_total.pack(side="left", padx=5)

    # Função para calcular o valor total
    def calcular_total():
        total = 0
        for item in itens_selecionados:
            if item['var'].get() == 1:
                total += item['preco'] * item['quantidade'].get()
        label_total.config(text=f"R$ {total:.2f}")
        return total

    # Botão para calcular o total
    ttk.Button(janela, text="Calcular Total", command=calcular_total, style='TButton').pack(pady=10)

    # Botão para criar o pedido
    ttk.Button(janela, text="Criar Pedido", command=lambda: criar_pedido(
        entry_mesa.get(),
        [{'id': item['id'], 'quantidade': item['quantidade'].get()} for item in itens_selecionados if item['var'].get() == 1],
        calcular_total()
    ), style='TButton').pack(pady=10)

    # Botão para voltar ao menu principal
    ttk.Button(janela, text="Voltar", command=lambda: [janela.destroy(), callback_voltar()], style='TButton').pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    tela_pedidos(root, lambda: None)
    root.mainloop()