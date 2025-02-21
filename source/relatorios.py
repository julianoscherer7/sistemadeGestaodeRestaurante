# relatorios.py
import tkinter as tk
from tkinter import messagebox
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

def tela_relatorios():
    janela = tk.Tk()
    janela.title("Gerar Relatórios")

    tk.Label(janela, text="Clique no botão para gerar o relatório de pedidos.").pack(pady=20)

    # Botão para gerar o relatório
    tk.Button(janela, text="Gerar Relatório", command=gerar_relatorio_pedidos).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    tela_relatorios()