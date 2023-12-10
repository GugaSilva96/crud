import tkinter as tk
from tkinter import ttk
import sqlite3

class CRUDApp:
    def __init__(self, root):
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
        # Frame para entrada de dados
        self.data_frame = ttk.Frame(self.root, padding="10")
        self.data_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels e entradas para dados do cliente
        ttk.Label(self.data_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.nome_entry = ttk.Entry(self.data_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(self.data_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.email_entry = ttk.Entry(self.data_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(self.data_frame, text="Telefone:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.telefone_entry = ttk.Entry(self.data_frame)
        self.telefone_entry.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Botões CRUD
        ttk.Button(self.data_frame, text="Criar", command=self.create_record).grid(row=3, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(self.data_frame, text="Ler", command=self.read_records).grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(self.data_frame, text="Atualizar", command=self.update_record).grid(row=3, column=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(self.data_frame, text="Excluir", command=self.delete_record).grid(row=3, column=3, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Lista para exibir registros
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Email", "Telefone"), show="headings", height=10)
        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefone", text="Telefone")

        # Preencher a lista com registros existentes
        self.read_records()

    def create_record(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        if nome and email:
            self.cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
            self.connection.commit()
            self.clear_entries()
            self.read_records()

    def read_records(self):
        # Limpar a lista antes de exibir os registros
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Buscar registros no banco de dados
        self.cursor.execute("SELECT * FROM clientes")
        records = self.cursor.fetchall()

        # Adicionar registros à lista
        for row in records:
            self.tree.insert("", "end", values=row)

    def update_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            record_id = self.tree.item(selected_item, "values")[0]
            nome = self.nome_entry.get()
            email = self.email_entry.get()
            telefone = self.telefone_entry.get()

            if nome and email:
                self.cursor.execute("UPDATE clientes SET nome=?, email=?, telefone=? WHERE id=?", (nome, email, telefone, record_id))
                self.connection.commit()
                self.clear_entries()
                self.read_records()

    def delete_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            record_id = self.tree.item(selected_item, "values")[0]
            self.cursor.execute("DELETE FROM clientes WHERE id=?", (record_id,))
            self.connection.commit()
            self.clear_entries()
            self.read_records()

    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
