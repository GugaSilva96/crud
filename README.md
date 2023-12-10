# CRUD App em Tkinter e SQLite

## Descrição
Este é um aplicativo CRUD (Create, Read, Update, Delete) simples implementado em Tkinter e SQLite. O aplicativo permite gerenciar registros de clientes, realizando operações básicas de banco de dados.

## Código-fonte
```python
import tkinter as tk
from tkinter import ttk
import sqlite3

class CRUDApp:
    def __init__(self, root):
        # Inicialização da aplicação
        self.root = root
        self.root.title("CRUD App")

        # Conectar ao banco de dados SQLite (será criado se não existir)
        self.connection = sqlite3.connect("crud_database.db")
        self.cursor = self.connection.cursor()

        # Criar a tabela se não existir
        self.create_table()

        # Criar os widgets
        self.create_widgets()

    def create_table(self):
        # Método para criar a tabela no banco de dados
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT
            )
        ''')
        self.connection.commit()

    def create_widgets(self):
        # Método para criar os widgets da interface gráfica
        # ... (código omitido para brevidade)

    def create_record(self):
        # Método para criar um novo registro
        # ... (código omitido para brevidade)

    def read_records(self):
        # Método para ler registros do banco de dados e exibi-los na lista
        # ... (código omitido para brevidade)

    def update_record(self):
        # Método para atualizar um registro existente
        # ... (código omitido para brevidade)

    def delete_record(self):
        # Método para excluir um registro
        # ... (código omitido para brevidade)

    def clear_entries(self):
        # Método para limpar as entradas de texto
        # ... (código omitido para brevidade)

if __name__ == "__main__":
    # Criação da instância da aplicação e execução do loop principal
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()

