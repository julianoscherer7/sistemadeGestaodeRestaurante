import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from datetime import datetime
from database import conectar  # Importe a função de conexão com o banco de dados

def tela_pedidos(parent, callback_principal):
    """Cria a tela de gerenciamento de pedidos."""
    class TelaPedidos:
        def __init__(self):
            # Configuração da janela
            self.parent = parent
            self.frame = tk.Frame(parent, bg="#2C3E50")
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Fonte moderna
            self.fonte_titulo = Font(family="Helvetica", size=24, weight="bold")
            self.fonte_texto = Font(family="Helvetica", size=12)
            self.fonte_preco = Font(family="Helvetica", size=12, weight="bold")

            # Lista de pedidos
            self.pedidos = []
            self.pedido_atual = {"mesa": None, "itens": {}, "horario": None}

            # Lista de mesas registradas (puxada do banco de dados)
            self.mesas_registradas = self.carregar_mesas()

            # Tela inicial com botões
            self.tela_inicial()

        def carregar_mesas(self):
            """Carrega as mesas registradas do banco de dados."""
            conexao = conectar()
            if conexao:
                cursor = conexao.cursor()
                cursor.execute("SELECT Numero FROM Mesas")
                mesas = [str(mesa[0]) for mesa in cursor.fetchall()]
                conexao.close()
                return mesas
            return []

        def tela_inicial(self):
            """Exibe a tela inicial com botões para novo pedido e ver pedidos."""
            self.limpar_tela()

            # Botão para novo pedido
            botao_novo_pedido = tk.Button(
                self.frame,
                text="Novo Pedido",
                font=self.fonte_titulo,
                bg="#3498DB",
                fg="#FFFFFF",
                activebackground="#2980B9",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.novo_pedido
            )
            botao_novo_pedido.pack(pady=20)

            # Botão para ver pedidos
            botao_ver_pedidos = tk.Button(
                self.frame,
                text="Ver Pedidos",
                font=self.fonte_titulo,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.ver_pedidos
            )
            botao_ver_pedidos.pack(pady=20)

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
                command=self.fechar_janela
            )
            botao_voltar.pack(pady=20)

        def novo_pedido(self):
            """Exibe a tela para criar um novo pedido."""
            self.limpar_tela()

            # Título
            titulo = tk.Label(self.frame, text="Novo Pedido", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            titulo.pack(pady=20)

            # Frame para seleção de mesa
            frame_mesa = tk.Frame(self.frame, bg="#2C3E50")
            frame_mesa.pack(fill="x", pady=10)

            label_mesa = tk.Label(frame_mesa, text="Número da Mesa:", font=self.fonte_texto, fg="#ECF0F1", bg="#2C3E50")
            label_mesa.pack(side="left", padx=10, pady=5)

            self.entry_mesa = ttk.Combobox(frame_mesa, font=self.fonte_texto, width=10)
            self.entry_mesa["values"] = self.mesas_registradas
            self.entry_mesa.pack(side="left", padx=10, pady=5)

            # Frame para a lista de produtos com barra de rolagem
            self.canvas = tk.Canvas(self.frame, bg="#2C3E50", highlightthickness=0)
            self.canvas.pack(side="left", fill="both", expand=True)

            scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
            scrollbar.pack(side="right", fill="y")

            self.canvas.configure(yscrollcommand=scrollbar.set)
            self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            frame_produtos = tk.Frame(self.canvas, bg="#2C3E50")
            self.canvas.create_window((0, 0), window=frame_produtos, anchor="nw")

            # Lista de itens do cardápio
            self.itens_cardapio = [
                {"nome": "Hambúrguer Clássico", "preco": 25.00, "tipo": "comida"},
                {"nome": "Hambúrguer Vegetariano", "preco": 22.00, "tipo": "comida"},
                {"nome": "Pizza Margherita", "preco": 35.00, "tipo": "comida"},
                {"nome": "Sushi Sashimi", "preco": 45.00, "tipo": "comida"},
                {"nome": "Coca-Cola", "preco": 8.00, "tipo": "bebida"},
                {"nome": "Suco de Laranja", "preco": 10.00, "tipo": "bebida"},
                {"nome": "Cerveja Artesanal", "preco": 15.00, "tipo": "bebida"},
                {"nome": "Vinho Tinto", "preco": 25.00, "tipo": "bebida"},
                {"nome": "Água Mineral", "preco": 5.00, "tipo": "bebida"},
                {"nome": "Café Expresso", "preco": 6.00, "tipo": "bebida"},
                {"nome": "Batata Frita", "preco": 12.00, "tipo": "comida"},
                {"nome": "Frango à Parmegiana", "preco": 40.00, "tipo": "comida"},
                {"nome": "Espaguete à Carbonara", "preco": 30.00, "tipo": "comida"},
                {"nome": "Salada de Frutas", "preco": 15.00, "tipo": "comida"},
                {"nome": "Sorvete de Chocolate", "preco": 10.00, "tipo": "comida"},
                {"nome": "Torta de Limão", "preco": 18.00, "tipo": "comida"},
                {"nome": "Refrigerante", "preco": 7.00, "tipo": "bebida"},
                {"nome": "Suco de Uva", "preco": 10.00, "tipo": "bebida"},
                {"nome": "Cerveja Pilsen", "preco": 12.00, "tipo": "bebida"},
                {"nome": "Caipirinha de Limão", "preco": 20.00, "tipo": "bebida"},
                {"nome": "Lasanha à Bolonhesa", "preco": 40.00, "tipo": "comida"},
                {"nome": "Risoto de Cogumelos", "preco": 45.00, "tipo": "comida"},
                {"nome": "Risoto de Camarão", "preco": 50.00, "tipo": "comida"},
                {"nome": "Salada Caesar", "preco": 20.00, "tipo": "comida"},
                {"nome": "Salada Grega", "preco": 18.00, "tipo": "comida"},
                {"nome": "Macarrão à Carbonara", "preco": 32.00, "tipo": "comida"},
                {"nome": "Macarrão ao Molho Pesto", "preco": 30.00, "tipo": "comida"},
                {"nome": "Filé Mignon", "preco": 60.00, "tipo": "comida"},
                {"nome": "Strogonoff de Carne", "preco": 35.00, "tipo": "comida"},
                {"nome": "Strogonoff de Frango", "preco": 30.00, "tipo": "comida"}
            ]

            # Exibe os itens do cardápio divididos em comidas e bebidas
            label_comidas = tk.Label(frame_produtos, text="Comidas", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            label_comidas.pack(pady=10)

            # Frame para as comidas (duas colunas)
            frame_comidas = tk.Frame(frame_produtos, bg="#2C3E50")
            frame_comidas.pack(fill="x", pady=5)

            # Coluna 1 de comidas
            frame_coluna1 = tk.Frame(frame_comidas, bg="#2C3E50")
            frame_coluna1.pack(side="left", fill="both", expand=True, padx=10)

            for item in self.itens_cardapio[:15]:  # Primeiras 15 comidas
                if item["tipo"] == "comida":
                    self.criar_item_cardapio(frame_coluna1, item)

            # Coluna 2 de comidas
            frame_coluna2 = tk.Frame(frame_comidas, bg="#2C3E50")
            frame_coluna2.pack(side="right", fill="both", expand=True, padx=10)

            for item in self.itens_cardapio[15:]:  # Últimas 15 comidas
                if item["tipo"] == "comida":
                    self.criar_item_cardapio(frame_coluna2, item)

            label_bebidas = tk.Label(frame_produtos, text="Bebidas", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            label_bebidas.pack(pady=10)

            for item in self.itens_cardapio:
                if item["tipo"] == "bebida":
                    self.criar_item_cardapio(frame_produtos, item)

            # Frame para o pedido atual
            frame_pedido_atual = tk.Frame(self.frame, bg="#2C3E50")
            frame_pedido_atual.pack(fill="x", pady=20)

            self.label_pedido_atual = tk.Label(frame_pedido_atual, text="Pedido Atual:", font=self.fonte_texto, fg="#ECF0F1", bg="#2C3E50")
            self.label_pedido_atual.pack(side="left", padx=10, pady=5)

            self.label_total = tk.Label(frame_pedido_atual, text="Total: R$ 0.00", font=self.fonte_preco, fg="#2ECC71", bg="#2C3E50")
            self.label_total.pack(side="right", padx=10, pady=5)

            # Botão para finalizar pedido
            botao_finalizar = tk.Button(
                self.frame,
                text="Finalizar Pedido",
                font=self.fonte_texto,
                bg="#2ECC71",
                fg="#FFFFFF",
                activebackground="#27AE60",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.finalizar_pedido
            )
            botao_finalizar.pack(pady=20)

            # Botão para voltar à tela inicial
            botao_voltar = tk.Button(
                self.frame,
                text="Voltar",
                font=self.fonte_texto,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.tela_inicial
            )
            botao_voltar.pack(pady=20)

        def criar_item_cardapio(self, frame_produtos, item):
            """Cria um item do cardápio na tela."""
            frame_item = tk.Frame(frame_produtos, bg="#34495E", bd=2, relief="groove")
            frame_item.pack(fill="x", pady=5, padx=10)

            label_item = tk.Label(frame_item, text=item["nome"], font=self.fonte_texto, fg="#ECF0F1", bg="#34495E")
            label_item.pack(side="left", padx=10, pady=5)

            label_preco = tk.Label(frame_item, text=f"R$ {item['preco']:.2f}", font=self.fonte_preco, fg="#2ECC71", bg="#34495E")
            label_preco.pack(side="left", padx=10, pady=5)

            # Label para quantidade
            label_quantidade = tk.Label(frame_item, text="0", font=self.fonte_texto, fg="#ECF0F1", bg="#34495E")
            label_quantidade.pack(side="left", padx=10, pady=5)

            # Botão para adicionar item
            botao_mais = tk.Button(
                frame_item,
                text="+",
                font=self.fonte_texto,
                bg="#3498DB",
                fg="#FFFFFF",
                activebackground="#2980B9",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=10,
                pady=5,
                command=lambda nome=item["nome"]: self.adicionar_item(nome, label_quantidade)
            )
            botao_mais.pack(side="right", padx=5, pady=5)

            # Botão para remover item
            botao_menos = tk.Button(
                frame_item,
                text="-",
                font=self.fonte_texto,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=10,
                pady=5,
                command=lambda nome=item["nome"]: self.remover_item(nome, label_quantidade)
            )
            botao_menos.pack(side="right", padx=5, pady=5)

        def adicionar_item(self, nome, label_quantidade):
            """Adiciona um item ao pedido atual."""
            if nome in self.pedido_atual["itens"]:
                self.pedido_atual["itens"][nome] += 1
            else:
                self.pedido_atual["itens"][nome] = 1
            label_quantidade.config(text=str(self.pedido_atual["itens"][nome]))
            self.atualizar_pedido_atual()

        def remover_item(self, nome, label_quantidade):
            """Remove um item do pedido atual."""
            if nome in self.pedido_atual["itens"]:
                if self.pedido_atual["itens"][nome] > 1:
                    self.pedido_atual["itens"][nome] -= 1
                else:
                    del self.pedido_atual["itens"][nome]
                label_quantidade.config(text=str(self.pedido_atual["itens"].get(nome, 0)))
            self.atualizar_pedido_atual()

        def atualizar_pedido_atual(self):
            """Atualiza a exibição do pedido atual."""
            texto_pedido = "Pedido Atual:\n"
            total = 0

            for nome, quantidade in self.pedido_atual["itens"].items():
                item = next(item for item in self.itens_cardapio if item["nome"] == nome)
                texto_pedido += f"{nome} x {quantidade} = R$ {item['preco'] * quantidade:.2f}\n"
                total += item["preco"] * quantidade

            self.label_pedido_atual.config(text=texto_pedido)
            self.label_total.config(text=f"Total: R$ {total:.2f}")

        def finalizar_pedido(self):
            """Finaliza o pedido atual e o adiciona à lista de pedidos."""
            mesa = self.entry_mesa.get()
            if mesa and self.pedido_atual["itens"]:
                self.pedido_atual["mesa"] = mesa
                self.pedido_atual["horario"] = datetime.now()
                self.pedidos.append(self.pedido_atual)
                self.pedido_atual = {"mesa": None, "itens": {}, "horario": None}
                self.tela_inicial()

        def ver_pedidos(self):
            """Exibe a tela para visualizar os pedidos."""
            self.limpar_tela()

            # Título
            titulo = tk.Label(self.frame, text="Pedidos Realizados", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            titulo.pack(pady=20)

            # Frame para a lista de pedidos
            frame_pedidos = tk.Frame(self.frame, bg="#2C3E50")
            frame_pedidos.pack(fill="both", expand=True, padx=10, pady=10)

            # Ordena os pedidos por horário (mais recentes primeiro)
            self.pedidos.sort(key=lambda x: x["horario"], reverse=True)

            # Exibe os pedidos
            for pedido in self.pedidos:
                frame_pedido = tk.Frame(frame_pedidos, bg="#34495E", bd=2, relief="groove")
                frame_pedido.pack(fill="x", pady=5, padx=10)

                # Calcula o total do pedido
                total_pedido = sum(
                    next(item["preco"] for item in self.itens_cardapio if item["nome"] == nome) * quantidade
                    for nome, quantidade in pedido["itens"].items()
                )

                label_pedido = tk.Label(
                    frame_pedido,
                    text=f"Pedido {self.pedidos.index(pedido) + 1} | Mesa {pedido['mesa']} | {pedido['horario'].strftime('%H:%M')} | Total: R$ {total_pedido:.2f}",
                    font=self.fonte_texto,
                    fg="#ECF0F1",
                    bg="#34495E"
                )
                label_pedido.pack(side="left", padx=10, pady=5)

                # Botão para editar pedido
                botao_editar = tk.Button(
                    frame_pedido,
                    text="Editar",
                    font=self.fonte_texto,
                    bg="#3498DB",
                    fg="#FFFFFF",
                    activebackground="#2980B9",
                    activeforeground="#FFFFFF",
                    relief="flat",
                    bd=0,
                    padx=10,
                    pady=5,
                    command=lambda p=pedido: self.editar_pedido(p)
                )
                botao_editar.pack(side="right", padx=5, pady=5)

                # Botão para excluir pedido
                botao_excluir = tk.Button(
                    frame_pedido,
                    text="Excluir",
                    font=self.fonte_texto,
                    bg="#E74C3C",
                    fg="#FFFFFF",
                    activebackground="#C0392B",
                    activeforeground="#FFFFFF",
                    relief="flat",
                    bd=0,
                    padx=10,
                    pady=5,
                    command=lambda p=pedido: self.excluir_pedido(p)
                )
                botao_excluir.pack(side="right", padx=5, pady=5)

            # Botão para voltar à tela inicial
            botao_voltar = tk.Button(
                self.frame,
                text="Voltar",
                font=self.fonte_texto,
                bg="#E74C3C",
                fg="#FFFFFF",
                activebackground="#C0392B",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.tela_inicial
            )
            botao_voltar.pack(pady=20)

        def editar_pedido(self, pedido):
            """Edita um pedido existente."""
            self.pedido_atual = pedido
            self.pedidos.remove(pedido)
            self.novo_pedido()

        def excluir_pedido(self, pedido):
            """Exclui um pedido existente."""
            self.pedidos.remove(pedido)
            self.ver_pedidos()

        def limpar_tela(self):
            """Limpa a tela atual."""
            for widget in self.frame.winfo_children():
                widget.destroy()

        def fechar_janela(self):
            """Fecha a tela de pedidos e retorna à tela principal."""
            self.frame.pack_forget()
            callback_principal()

        def mostrar(self):
            """Mostra a tela de pedidos."""
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        def ocultar(self):
            """Oculta a tela de pedidos."""
            self.frame.pack_forget()

    return TelaPedidos()