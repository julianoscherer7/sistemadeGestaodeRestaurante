# Sistema de Gestão de Restaurante

Este é um sistema de gestão para restaurantes, desenvolvido em Python com a biblioteca Tkinter para a interface gráfica e MySQL para o banco de dados. O sistema permite gerenciar mesas, pedidos, cardápio e gerar relatórios.

---

## Funcionalidades

1. **Login e Autenticação:**
   - Tela de login com autenticação de usuários.
   - Opção para cadastrar novos usuários.

2. **Gerenciamento de Mesas:**
   - Adicionar, visualizar e limpar mesas.
   - Status das mesas (Livre/Ocupada) com cores indicativas (verde/vermelho).

3. **Gerenciamento de Pedidos:**
   - Criar novos pedidos associados a uma mesa.
   - Adicionar itens do cardápio ao pedido.
   - Visualizar e editar pedidos existentes.

4. **Gerenciamento de Cardápio:**
   - Lista de comidas e bebidas disponíveis.
   - Adicionar novos itens ao cardápio (não implementado no código atual).

5. **Relatórios:**
   - Gerar relatórios de pedidos em formato PDF.

---

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Interface Gráfica:** Tkinter
- **Banco de Dados:** MySQL
- **Geração de PDF:** ReportLab

---

## Como Executar o Projeto

### Pré-requisitos

1. Instale o Python (versão 3.8 ou superior).
2. Instale o MySQL Server e crie um banco de dados chamado `restaurante`.
3. Instale as dependências do projeto:
   ```bash
   pip install mysql-connector-python reportlab

   