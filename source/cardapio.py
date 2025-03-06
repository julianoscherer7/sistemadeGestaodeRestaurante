import tkinter as tk
from tkinter.font import Font

def tela_cardapio(parent, callback_principal):
    """Cria a tela de cardápio."""
    class TelaCardapio:
        def __init__(self):
            # Configuração da janela
            self.parent = parent
            self.frame = tk.Frame(parent, bg="#2C3E50")
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Fonte moderna
            self.fonte_titulo = Font(family="Helvetica", size=24, weight="bold")
            self.fonte_texto = Font(family="Helvetica", size=12)
            self.fonte_preco = Font(family="Helvetica", size=12, weight="bold")

            # Título
            titulo = tk.Label(self.frame, text="Cardápio", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            titulo.pack(pady=20)

            # Frame para o cardápio com barra de rolagem
            self.canvas = tk.Canvas(self.frame, bg="#2C3E50", highlightthickness=0)
            self.canvas.pack(side="left", fill="both", expand=True)

            scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
            scrollbar.pack(side="right", fill="y")

            self.canvas.configure(yscrollcommand=scrollbar.set)
            self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            frame_cardapio = tk.Frame(self.canvas, bg="#2C3E50")
            self.canvas.create_window((0, 0), window=frame_cardapio, anchor="nw")

            # Lista de comidas
            comidas = [
                ("Hambúrguer Clássico", "R$ 25,00"),
                ("Hambúrguer Vegetariano", "R$ 22,00"),
                ("Hambúrguer de Frango", "R$ 20,00"),
                ("Pizza Margherita", "R$ 35,00"),
                ("Pizza Calabresa", "R$ 38,00"),
                ("Pizza Quatro Queijos", "R$ 40,00"),
                ("Sushi Sashimi", "R$ 45,00"),
                ("Sushi Hot Roll", "R$ 30,00"),
                ("Sushi Temaki", "R$ 28,00"),
                ("Filé Mignon", "R$ 60,00"),
                ("Strogonoff de Carne", "R$ 35,00"),
                ("Strogonoff de Frango", "R$ 30,00"),
                ("Lasanha à Bolonhesa", "R$ 40,00"),
                ("Lasanha de Frango", "R$ 38,00"),
                ("Risoto de Cogumelos", "R$ 45,00"),
                ("Risoto de Camarão", "R$ 50,00"),
                ("Salada Caesar", "R$ 20,00"),
                ("Salada Grega", "R$ 18,00"),
                ("Macarrão à Carbonara", "R$ 32,00"),
                ("Macarrão ao Molho Pesto", "R$ 30,00")
            ]

            # Lista de bebidas
            bebidas = [
                ("Coca-Cola", "R$ 8,00"),
                ("Guaraná", "R$ 7,00"),
                ("Suco de Laranja", "R$ 10,00"),
                ("Suco de Maracujá", "R$ 10,00"),
                ("Água Mineral", "R$ 5,00"),
                ("Cerveja Artesanal", "R$ 15,00"),
                ("Vinho Tinto", "R$ 25,00"),
                ("Caipirinha", "R$ 18,00"),
                ("Chá Gelado", "R$ 7,00"),
                ("Café Expresso", "R$ 6,00")
            ]

            # Exibe as comidas
            for i, (comida, preco) in enumerate(comidas):
                frame_item = tk.Frame(frame_cardapio, bg="#34495E", bd=2, relief="groove")
                frame_item.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

                label_item = tk.Label(frame_item, text=comida, font=self.fonte_texto, fg="#ECF0F1", bg="#34495E")
                label_item.pack(side="left", padx=10, pady=5)

                label_preco = tk.Label(frame_item, text=preco, font=self.fonte_preco, fg="#2ECC71", bg="#34495E")
                label_preco.pack(side="right", padx=10, pady=5)

            # Exibe as bebidas
            for i, (bebida, preco) in enumerate(bebidas):
                frame_item = tk.Frame(frame_cardapio, bg="#34495E", bd=2, relief="groove")
                frame_item.grid(row=i, column=1, sticky="ew", padx=10, pady=5)

                label_item = tk.Label(frame_item, text=bebida, font=self.fonte_texto, fg="#ECF0F1", bg="#34495E")
                label_item.pack(side="left", padx=10, pady=5)

                label_preco = tk.Label(frame_item, text=preco, font=self.fonte_preco, fg="#2ECC71", bg="#34495E")
                label_preco.pack(side="right", padx=10, pady=5)

            # Botão para voltar à tela principal
            botao_voltar = tk.Button(
                self.frame,
                text="Voltar para Principal",
                font=self.fonte_texto,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.fechar_janela  # Fecha a tela de cardápio e abre a tela principal
            )
            botao_voltar.pack(pady=20)

        def fechar_janela(self):
            """Fecha a tela de cardápio e retorna à tela principal."""
            self.frame.pack_forget()  # Oculta o frame atual
            callback_principal()  # Abre a tela principal

        def mostrar(self):
            """Mostra a tela de cardápio."""
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        def ocultar(self):
            """Oculta a tela de cardápio."""
            self.frame.pack_forget()

    return TelaCardapio()