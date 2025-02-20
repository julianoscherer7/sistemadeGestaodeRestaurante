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

        pdf = canvas.Canvas("relatorio_pedidos.pdf", pagesize=letter)
        pdf.drawString(100, 750, "Relatório de Pedidos")

        y = 700
        for pedido in pedidos:
            pdf.drawString(100, y, f"Pedido ID: {pedido[0]} - Mesa: {pedido[1]} - Data: {pedido[2]} - Status: {pedido[3]}")
            y -= 20

        pdf.save()
        print("Relatório gerado com sucesso!")
    else:
        print("Falha ao conectar ao banco de dados.")