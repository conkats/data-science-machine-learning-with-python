import sys
import sqlite3
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QMessageBox


# Create and initialize the SQLite database
def create_database():
    db = sqlite3.connect('eproject_db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Projects (
            ID INTEGER PRIMARY KEY,
            Title varchar(100),
            Author varchar(100),
            Qty int
        )
    ''')
    db.commit()
    return db


# Console-based functions for managing projects
def add_project(cursor):
    id = int(input('Enter project ID: '))
    title = input('Enter project title: ')
    author = input('Enter project author: ')
    qty = int(input('Enter project quantity: '))
    cursor.execute('''INSERT INTO Projects (ID, Title, Author, Qty) VALUES (?, ?, ?, ?)''', (id, title, author, qty))


def update_project(cursor):
    id = int(input('Enter project ID to update: '))
    title = input('Enter new title: ')
    author = input('Enter new author: ')
    qty = int(input('Enter new quantity: '))
    cursor.execute('''UPDATE Projects SET Title = ?, Author = ?, Qty = ? WHERE ID = ?''', (title, author, qty, id))


def delete_project(cursor):
    id = int(input('Enter project ID to delete: '))
    cursor.execute('DELETE FROM Projects WHERE ID = ?', (id,))


def search_project(cursor):
    search_term = input("Enter search term: ")
    cursor.execute('SELECT * FROM Projects WHERE Title LIKE ? OR Author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def view_projectdb(cursor):
    cursor.execute('SELECT * FROM Projects')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def savedb_csv(cursor):
    cursor.execute('SELECT * FROM Projects')
    rows = cursor.fetchall()
    with open('Projects.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Author', 'Qty'])
        writer.writerows(rows)
    print("Data has been saved to Projects.csv")


# PyQt5 GUI Implementation
class ProjectManagerGUI(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.cursor = db.cursor()
        self.setWindowTitle("Project Manager")
        self.setGeometry(300, 300, 600, 400)
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # Buttons for various actions
        self.addButton = QPushButton("Add Project")
        self.addButton.clicked.connect(self.add_project)

        self.updateButton = QPushButton("Update Project")
        self.updateButton.clicked.connect(self.update_project)

        self.deleteButton = QPushButton("Delete Project")
        self.deleteButton.clicked.connect(self.delete_project)

        self.viewButton = QPushButton("View All Projects")
        self.viewButton.clicked.connect(self.view_projects)

        self.saveButton = QPushButton("Save to CSV")
        self.saveButton.clicked.connect(self.save_to_csv)

        # Add buttons to the layout
        layout.addWidget(self.addButton)
        layout.addWidget(self.updateButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.viewButton)
        layout.addWidget(self.saveButton)

        # Set up a table to display projects
        self.projectTable = QTableWidget()
        self.projectTable.setRowCount(0)
        self.projectTable.setColumnCount(4)
        self.projectTable.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Qty'])
        layout.addWidget(self.projectTable)

        self.setLayout(layout)

    def add_project(self):
        id, title, author, qty = self.get_project_details()
        if id and title and author and qty:
            self.cursor.execute('INSERT INTO Projects (ID, Title, Author, Qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
            self.db.commit()
            QMessageBox.information(self, "Success", "Project added successfully")
            self.view_projects()

    def update_project(self):
        id, title, author, qty = self.get_project_details()
        if id and title and author and qty:
            self.cursor.execute('UPDATE Projects SET Title = ?, Author = ?, Qty = ? WHERE ID = ?', (title, author, qty, id))
            self.db.commit()
            QMessageBox.information(self, "Success", "Project updated successfully")
            self.view_projects()

    def delete_project(self):
        id, _, _, _ = self.get_project_details()
        if id:
            self.cursor.execute('DELETE FROM Projects WHERE ID = ?', (id,))
            self.db.commit()
            QMessageBox.information(self, "Success", "Project deleted successfully")
            self.view_projects()

    def view_projects(self):
        self.cursor.execute('SELECT * FROM Projects')
        rows = self.cursor.fetchall()
        self.projectTable.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.projectTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.projectTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def save_to_csv(self):
        savedb_csv(self.cursor)
        QMessageBox.information(self, "Success", "Projects saved to CSV successfully")

    def get_project_details(self):
        id, ok = self.get_user_input("Enter Project ID")
        title, ok = self.get_user_input("Enter Project Title")
        author, ok = self.get_user_input("Enter Project Author")
        qty, ok = self.get_user_input("Enter Quantity")
        return int(id) if id else None, title, author, int(qty) if qty else None

    def get_user_input(self, prompt):
        text, ok = QInputDialog.getText(self, "Input", prompt)
        return text, ok


# Main function to choose between terminal or GUI
def main():
    db = create_database()
    user_choice = input("Enter 'T' for terminal mode or 'G' for GUI mode: ").upper()

    if user_choice == 'T':
        cursor = db.cursor()
        while True:
            user_choice = int(input(usage_message))
            if user_choice == 1:
                add_project(cursor)
                db.commit()
            elif user_choice == 2:
                update_project(cursor)
                db.commit()
            elif user_choice == 3:
                delete_project(cursor)
                db.commit()
            elif user_choice == 4:
                search_project(cursor)
            elif user_choice == 5:
                view_projectdb(cursor)
            elif user_choice == 6:
                savedb_csv(cursor)
            elif user_choice == 0:
                db.close()
                break
            else:
                print("Invalid choice. Please try again.")
    elif user_choice == 'G':
        app = QApplication(sys.argv)
        window = ProjectManagerGUI(db)
        window.show()
        sys.exit(app.exec_())
    else:
        print("Invalid option. Please choose 'T' or 'G'.")


if __name__ == "__main__":
    main()

