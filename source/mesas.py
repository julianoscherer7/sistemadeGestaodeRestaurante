import tkinter as tk
from tkinter.font import Font
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
    else:
        print("Falha ao conectar ao banco de dados.")
        return False

def tela_mesas(parent, callback_principal):
    """Cria a tela de gerenciamento de mesas."""
    def atualizar_mesas():
        """Atualiza a lista de mesas exibidas na tela."""
        # Limpa o frame das mesas
        for widget in frame_mesas.winfo_children():
            widget.destroy()

        # Obtém as mesas do banco de dados
        mesas = listar_mesas()

        # Exibe um botão para cada mesa
        for i, mesa in enumerate(mesas):
            id_mesa, numero, capacidade, status = mesa

            # Define a cor do botão com base no status da mesa
            cor_fundo = "#2ECC71" if status == "Livre" else "#E74C3C"  # Verde para livre, vermelho para ocupada
            cor_texto = "#FFFFFF"

            # Cria o botão para a mesa
            botao_mesa = tk.Button(
                frame_mesas,
                text=f"Mesa {numero}\nCapacidade: {capacidade}\nStatus: {status}",
                font=fonte_texto,
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
            botao_mesa.grid(row=i // 4, column=i % 4, padx=10, pady=10)  # Organiza em uma grade 4x4

    def adicionar_mesa_handler():
        """Adiciona uma nova mesa ao banco de dados e atualiza a lista."""
        numero = entry_numero.get()
        capacidade = entry_capacidade.get()
        status = "Livre"  # Define o status inicial como "Livre"

        if numero and capacidade:
            if adicionar_mesa(numero, capacidade, status):
                atualizar_mesas()  # Atualiza a lista de mesas
                entry_numero.delete(0, tk.END)  # Limpa o campo de número
                entry_capacidade.delete(0, tk.END)  # Limpa o campo de capacidade
            else:
                label_erro.config(text="Erro ao adicionar mesa!", fg="#E74C3C")
        else:
            label_erro.config(text="Preencha todos os campos!", fg="#E74C3C")

    def fechar_janela():
        """Fecha a tela de mesas e retorna à tela principal."""
        frame.pack_forget()  # Oculta o frame atual
        callback_principal()  # Reconstroi ou reexibe a tela principal

    # Configuração da janela
    janela = parent
    janela.title("Mesas")
    janela.geometry("1024x768")
    janela.configure(bg="#2C3E50")

    # Frame principal
    frame = tk.Frame(janela, bg="#2C3E50")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Fonte moderna
    fonte_titulo = Font(family="Helvetica", size=24, weight="bold")
    fonte_texto = Font(family="Helvetica", size=12)

    # Título
    titulo = tk.Label(frame, text="Mesas Disponíveis", font=fonte_titulo, fg="#ECF0F1", bg="#2C3E50")
    titulo.pack(pady=20)

    # Botão para voltar à tela principal
    botao_voltar = tk.Button(
        frame,
        text="Voltar para Principal",
        font=fonte_texto,
        bg="#E74C3C",
        fg="#FFFFFF",
        activebackground="#C0392B",
        activeforeground="#FFFFFF",
        relief="flat",
        bd=0,
        padx=20,
        pady=10,
        command=fechar_janela  # Fecha a tela de mesas e abre a tela principal
    )
    botao_voltar.place(relx=0.95, rely=0.05, anchor="ne")  # Posiciona no canto superior direito

    # Frame para adicionar mesas
    frame_adicionar = tk.Frame(frame, bg="#2C3E50")
    frame_adicionar.pack(fill="x", pady=10)

    # Campo para número da mesa
    label_numero = tk.Label(frame_adicionar, text="Número da Mesa:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_numero.grid(row=0, column=0, padx=5, pady=5)
    entry_numero = tk.Entry(frame_adicionar, font=fonte_texto, width=10)
    entry_numero.grid(row=0, column=1, padx=5, pady=5)

    # Campo para capacidade da mesa
    label_capacidade = tk.Label(frame_adicionar, text="Capacidade:", font=fonte_texto, fg="#ECF0F1", bg="#2C3E50")
    label_capacidade.grid(row=0, column=2, padx=5, pady=5)
    entry_capacidade = tk.Entry(frame_adicionar, font=fonte_texto, width=10)
    entry_capacidade.grid(row=0, column=3, padx=5, pady=5)

    # Botão para adicionar mesa
    botao_adicionar = tk.Button(
        frame_adicionar,
        text="Adicionar Mesa",
        font=fonte_texto,
        bg="#3498DB",
        fg="#FFFFFF",
        activebackground="#2980B9",
        activeforeground="#FFFFFF",
        relief="flat",
        bd=0,
        padx=20,
        pady=10,
        command=adicionar_mesa_handler
    )
    botao_adicionar.grid(row=0, column=4, padx=10, pady=5)

    # Label para mensagens de erro
    label_erro = tk.Label(frame_adicionar, text="", font=fonte_texto, fg="#E74C3C", bg="#2C3E50")
    label_erro.grid(row=1, column=0, columnspan=5, pady=5)

    # Frame para os botões das mesas
    frame_mesas = tk.Frame(frame, bg="#2C3E50")
    frame_mesas.pack(fill="both", expand=True)

    # Atualiza a lista de mesas ao abrir a tela
    atualizar_mesas()

    # Funções para mostrar e ocultar a tela
    def mostrar():
        frame.pack(fill="both", expand=True, padx=20, pady=20)

    def ocultar():
        frame.pack_forget()

    # Retorna um objeto com as funções mostrar e ocultar
    return type('TelaMesas', (), {'mostrar': mostrar, 'ocultar': ocultar})()