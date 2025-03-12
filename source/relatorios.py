import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from database import conectar

def gerar_relatorio_pedidos():
    """Gera um relatório de pedidos em formato PDF."""
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
    """Cria a tela de relatórios com layout moderno."""
    class TelaRelatorios:
        def __init__(self):
            # Configuração da janela
            self.parent = parent
            self.frame = tk.Frame(parent, bg="#2C3E50")
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Fonte moderna
            self.fonte_titulo = ("Helvetica", 24, "bold")
            self.fonte_texto = ("Helvetica", 12)

            # Título
            titulo = tk.Label(self.frame, text="Relatórios", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            titulo.pack(pady=20)

            # Botão para gerar relatório de pedidos
            botao_gerar_relatorio = tk.Button(
                self.frame,
                text="Gerar Relatório de Pedidos",
                font=self.fonte_texto,
                bg="#3498DB",
                fg="#FFFFFF",
                activebackground="#2980B9",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=gerar_relatorio_pedidos
            )
            botao_gerar_relatorio.pack(pady=20)

            # Botão para voltar ao menu principal
            botao_voltar = tk.Button(
                self.frame,
                text="Voltar ao Menu Principal",
                font=self.fonte_texto,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.fechar_janela
            )
            botao_voltar.pack(pady=20)

        def fechar_janela(self):
            """Fecha a tela de relatórios e retorna ao menu principal."""
            self.frame.pack_forget()  # Oculta o frame atual
            callback_principal()  # Abre o menu principal

        def mostrar(self):
            """Mostra a tela de relatórios."""
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        def ocultar(self):
            """Oculta a tela de relatórios."""
            self.frame.pack_forget()

    return TelaRelatorios()

# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Gestão de Restaurante")

    def abrir_menu_principal():
        print("Menu principal aberto!")

    # Cria a tela de relatórios
    tela_relatorios_instance = tela_relatorios(root, abrir_menu_principal)
    tela_relatorios_instance.mostrar()

    root.mainloop()