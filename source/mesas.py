import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar

def listar_mesas():
    """Lista todas as mesas do banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Mesas")
        mesas = cursor.fetchall()
        conexao.close()
        return mesas
    return []

def adicionar_mesa(numero, capacidade, status):
    """Adiciona uma nova mesa ao banco de dados."""
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Mesas (Numero, Capacidade, Status) VALUES (%s, %s, %s)", (numero, capacidade, status))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar mesa: {e}")
            return False
        finally:
            conexao.close()
    return False

def atualizar_status_mesa(numero_mesa, status):
    """Atualiza o status de uma mesa no banco de dados."""
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("UPDATE Mesas SET Status = %s WHERE Numero = %s", (status, numero_mesa))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar status da mesa: {e}")
            return False
        finally:
            conexao.close()
    return False

def tela_mesas(parent, callback_principal):
    """Cria a tela de gerenciamento de mesas."""
    class TelaMesas:
        def __init__(self):
            # Configuração da janela
            self.parent = parent
            self.frame = tk.Frame(parent, bg="#2C3E50")
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Fonte moderna
            self.fonte_titulo = ("Helvetica", 24, "bold")
            self.fonte_texto = ("Helvetica", 12)

            # Título
            titulo = tk.Label(self.frame, text="Mesas Disponíveis", font=self.fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
            titulo.pack(pady=20)

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
            botao_voltar.place(relx=0.95, rely=0.05, anchor="ne")  # Posiciona no canto superior direito

            # Frame para adicionar mesas
            frame_adicionar = tk.Frame(self.frame, bg="#2C3E50")
            frame_adicionar.pack(fill="x", pady=10)

            # Campo para número da mesa
            label_numero = tk.Label(frame_adicionar, text="Número da Mesa:", font=self.fonte_texto, fg="#ECF0F1", bg="#2C3E50")
            label_numero.grid(row=0, column=0, padx=5, pady=5)
            self.entry_numero = tk.Entry(frame_adicionar, font=self.fonte_texto, width=10)
            self.entry_numero.grid(row=0, column=1, padx=5, pady=5)

            # Campo para capacidade da mesa
            label_capacidade = tk.Label(frame_adicionar, text="Capacidade:", font=self.fonte_texto, fg="#ECF0F1", bg="#2C3E50")
            label_capacidade.grid(row=0, column=2, padx=5, pady=5)
            self.entry_capacidade = tk.Entry(frame_adicionar, font=self.fonte_texto, width=10)
            self.entry_capacidade.grid(row=0, column=3, padx=5, pady=5)

            # Botão para adicionar mesa
            botao_adicionar = tk.Button(
                frame_adicionar,
                text="Adicionar Mesa",
                font=self.fonte_texto,
                bg="#3498DB",
                fg="#FFFFFF",
                activebackground="#2980B9",
                activeforeground="#FFFFFF",
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                command=self.adicionar_mesa_handler
            )
            botao_adicionar.grid(row=0, column=4, padx=10, pady=5)

            # Label para mensagens de erro
            self.label_erro = tk.Label(frame_adicionar, text="", font=self.fonte_texto, fg="#E74C3C", bg="#2C3E50")
            self.label_erro.grid(row=1, column=0, columnspan=5, pady=5)

            # Frame para os botões das mesas
            self.frame_mesas = tk.Frame(self.frame, bg="#2C3E50")
            self.frame_mesas.pack(fill="both", expand=True)

            # Atualiza a lista de mesas ao abrir a tela
            self.atualizar_mesas()

        def atualizar_mesas(self):
            """Atualiza a lista de mesas exibidas na tela."""
            # Limpa o frame das mesas
            for widget in self.frame_mesas.winfo_children():
                widget.destroy()

            # Obtém as mesas do banco de dados
            mesas = listar_mesas()

            # Exibe um botão para cada mesa
            for i, mesa in enumerate(mesas):
                id_mesa, numero, capacidade, status = mesa

                # Define a cor do botão com base no status da mesa
                cor_fundo = "#2ECC71" if status == "Livre" else "#E74C3C"  # Verde para livre, vermelho para ocupada
                cor_texto = "#FFFFFF"

                # Frame para cada mesa
                frame_mesa = tk.Frame(self.frame_mesas, bg="#34495E", bd=2, relief="groove")
                frame_mesa.grid(row=i // 4, column=i % 4, padx=10, pady=10)

                # Botão para a mesa
                botao_mesa = tk.Button(
                    frame_mesa,
                    text=f"Mesa {numero}\nCapacidade: {capacidade}\nStatus: {status}",
                    font=self.fonte_texto,
                    bg=cor_fundo,
                    fg=cor_texto,
                    activebackground=cor_fundo,
                    activeforeground=cor_texto,
                    relief="flat",
                    bd=0,
                    padx=20,
                    pady=10,
                    width=15,
                    height=5
                )
                botao_mesa.pack(pady=5)

                # Botão para limpar a mesa (se estiver ocupada)
                if status == "Ocupada":
                    botao_limpar = tk.Button(
                        frame_mesa,
                        text="Limpar Mesa",
                        font=self.fonte_texto,
                        bg="#3498DB",
                        fg="#FFFFFF",
                        activebackground="#2980B9",
                        activeforeground="#FFFFFF",
                        relief="flat",
                        bd=0,
                        padx=10,
                        pady=5,
                        command=lambda n=numero: self.limpar_mesa(n)
                    )
                    botao_limpar.pack(pady=5)

        def limpar_mesa(self, numero_mesa):
            """Altera o status da mesa para 'Livre' e atualiza a tela."""
            if atualizar_status_mesa(numero_mesa, "Livre"):
                self.atualizar_mesas()  # Atualiza a lista de mesas
            else:
                messagebox.showerror("Erro", "Falha ao limpar a mesa.")

        def adicionar_mesa_handler(self):
            """Adiciona uma nova mesa ao banco de dados e atualiza a lista."""
            numero = self.entry_numero.get()
            capacidade = self.entry_capacidade.get()
            status = "Livre"  # Define o status inicial como "Livre"

            if numero and capacidade:
                if adicionar_mesa(numero, capacidade, status):
                    self.atualizar_mesas()  # Atualiza a lista de mesas
                    self.entry_numero.delete(0, tk.END)  # Limpa o campo de número
                    self.entry_capacidade.delete(0, tk.END)  # Limpa o campo de capacidade
                else:
                    self.label_erro.config(text="Erro ao adicionar mesa!", fg="#E74C3C")
            else:
                self.label_erro.config(text="Preencha todos os campos!", fg="#E74C3C")

        def fechar_janela(self):
            """Fecha a tela de mesas e retorna à tela principal."""
            self.frame.pack_forget()  # Oculta o frame atual
            callback_principal()  # Abre a tela principal

        def mostrar(self):
            """Mostra a tela de mesas."""
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        def ocultar(self):
            """Oculta a tela de mesas."""
            self.frame.pack_forget()

    return TelaMesas()