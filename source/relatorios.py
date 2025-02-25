import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from database import conectar

def gerar_relatorio_pedidos():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Pedidos")
        pedidos = cursor.fetchall()
        conexao.close()

        # Cria o arquivo PDF
        pdf = canvas.Canvas("relatorio_pedidos.pdf", pagesize=letter)
        pdf.drawString(100, 750, "Relatório de Pedidos")

        y = 700  # Posição vertical inicial para os dados
        for pedido in pedidos:
            # Escreve os dados de cada pedido no PDF
            pdf.drawString(100, y, f"Pedido ID: {pedido[0]} - Mesa: {pedido[1]} - Data: {pedido[2]} - Status: {pedido[3]}")
            y -= 20  # Move para a próxima linha

        pdf.save()  # Salva o PDF
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso! Verifique o arquivo 'relatorio_pedidos.pdf'.")
    else:
        messagebox.showerror("Erro", "Falha ao conectar ao banco de dados.")

def tela_relatorios(parent, callback_principal):
    janela = tk.Toplevel(parent)
    janela.title("Gerar Relatórios")
    janela.geometry("600x400")
    janela.configure(bg="#2C3E50")

    # Frame principal
    frame = ttk.Frame(janela, padding="10")
    frame.pack(pady=10)

    # Título
    ttk.Label(frame, text="Gerar Relatórios", font=("Helvetica", 18, "bold"), background="#2C3E50", foreground="#ECF0F1").pack(pady=10)

    # Botão para gerar o relatório
    ttk.Button(
        frame,
        text="Gerar Relatório de Pedidos",
        command=gerar_relatorio_pedidos,
        style='TButton'
    ).pack(pady=20)

    # Botão para voltar à tela principal
    ttk.Button(
        frame,
        text="Voltar",
        command=lambda: [janela.destroy(), callback_principal()],
        style='TButton'
    ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    tela_relatorios(root, lambda: None)
    root.mainloop()