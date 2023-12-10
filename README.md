# Aplicativo CRUD em Python com Tkinter e SQLite

Este é um exemplo simples de um aplicativo CRUD (Create, Read, Update, Delete) desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite como o banco de dados.

## Requisitos

Certifique-se de ter o módulo `tkinter` instalado. Se não o tiver, você pode instalá-lo com o seguinte comando:

```bash
pip install tk
Estrutura do Código
O código está dividido em uma classe principal chamada CRUDApp. Aqui estão os principais componentes:

Inicialização do Aplicativo
python
Copy code
import tkinter as tk
from tkinter import ttk
import sqlite3

class CRUDApp:
    def __init__(self, root):
        # ...

        # Conectar ao banco de dados SQLite
        self.connection = sqlite3.connect("crud_database.db")
        self.cursor = self.connection.cursor()

        # Criar a tabela se não existir
        self.create_table()

        # Criar os widgets
        self.create_widgets()
Criação da Tabela
python
Copy code
def create_table(self):
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        )
    ''')
    self.connection.commit()
Configuração da Interface Gráfica
python
Copy code
def create_widgets(self):
    # ...

    # Labels e entradas para dados do cliente
    ttk.Label(self.data_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    self.nome_entry = ttk.Entry(self.data_frame)
    self.nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

    # ...

    # Botões CRUD
    ttk.Button(self.data_frame, text="Criar", command=self.create_record).grid(row=3, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
    ttk.Button(self.data_frame, text="Ler", command=self.read_records).grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
    ttk.Button(self.data_frame, text="Atualizar", command=self.update_record).grid(row=3, column=2, padx=5, pady=5, sticky=(tk.W, tk.E))
    ttk.Button(self.data_frame, text="Excluir", command=self.delete_record).grid(row=3, column=3, padx=5, pady=5, sticky=(tk.W, tk.E))

    # Lista para exibir registros
    self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Email", "Telefone"), show="headings", height=10)
    self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # ...
Operações CRUD
python
Copy code
def create_record(self):
    # ...

def read_records(self):
    # ...

def update_record(self):
    # ...

def delete_record(self):
    # ...
Limpeza de Entradas
python
Copy code
def clear_entries(self):
    self.nome_entry.delete(0, tk.END)
    self.email_entry.delete(0, tk.END)
    self.telefone_entry.delete(0, tk.END)
Execução do Aplicativo
python
Copy code
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
Este é um exemplo básico para fins educativos. Certifique-se de adaptar o código conforme necessário para atender aos requisitos específicos do seu projeto.

css
Copy code

Você pode copiar e colar esse conteúdo em um arquivo com a extensão `.md` para visualizá-lo como um documento Markdown.



