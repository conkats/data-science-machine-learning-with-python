# A program that can be used by a bookstore clerk.

import sqlite3
import csv 


usage_message = '''
# Welcome to the book system! 
# What would you like to do?

# 1 - Enter book.
# 2 - Update book.
# 3 - Delete book.
# 4 - Search books.
# 5 - View books in db.
# 6 - Save books to csv. 
# For all the options use ''.
# 0 - exit this program.
'''


def create_database():
    #try:
    # Creates or opens a file called book_db 
    # with a SQLite3 DB
    db = sqlite3.connect('ebookstore_db')
    
    # Get a cursor object
    cursor = db.cursor()

    #Remove every trace of the table during testing
    #cursor.execute('''
    #               DROP TABLE IF EXISTS Books
    #               ''')
    

    #rows = cursor.fetchall()
    #print("Initial data before adding any:")
    #for row in rows:
    #    print(row)
    

     # Check if table users does not exist and create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
      ID INTEGER PRIMARY KEY,
      TITLE varchar(100),
      Author varchar(100),
      Qty int
      )''')
        # Commit the change
    db.commit()
        
    #cursor = db.cursor()

    #books_= [(
    #     3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    #    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    #    (3003, 'The Lion, the Witch and the Warddrobe', 'C. S. Lewis', 25),
    #    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    #    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    #]
    #cursor.executemany('''
    #    INSERT INTO Books (ID, 
    #                         Title, 
    #                         Author, 
    #                         Qty)	
    #     VALUES(?,?,?,?)''', books_)

    #db.commit()
       # Catch the exception
    #except Exception as e:
    #    # Roll back any change if something goes wrong
    #    db.rollback()
    #    raise e
    #finally:
    #    # Close the db connection
    #    db.close()

    return db

def add_book(cursor):
    id= int(input('Enter book id :\n'))
    title = input('Enter book title :\n')
    author = input('Enter book author :\n')
    qty = int(input('Enter book quantity :\n'))
    cursor.execute('''INSERT INTO Books(id, title, author,qty)
                   VALUES(?,?,?,?)''', (id, title, author,qty)
                  )

def update_book(cursor):
    id= int(input('Enter book id to update :\n'))
    title = input('Enter new title :\n')
    author = input('Enter new author :\n')
    qty = int(input('Enter new quantity :\n'))
    cursor.execute('''UPDATE Books SET Title = ?, Author = ?, Qty = ? 
                   WHERE ID = ?''', (title, author, qty, id)
                  )

def delete_book(cursor):
    id= int(input('Enter book id to delete:\n'))
    cursor.execute('''DELETE FROM Books
                    WHERE ID = ?''', (id,)
                  )

#retrieve data from sql
def search_book(cursor):
    search_term = input("Enter search term: ")
    cursor.execute('''SELECT * FROM Books 
                   WHERE 
                   Title LIKE ? 
                   OR Author LIKE ?
                   OR ID LIKE ?''',
                    ('%' + search_term + '%', 
                     '%' + search_term + '%',
                     '%' + search_term + '%'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_bookdb(cursor):
    # Verify the deletion
    cursor.execute('SELECT * FROM Books')
    rows = cursor.fetchall()
    print("Data after deletion:")
    for row in rows:
        print(row)

def savedb_csv(cursor,db):
   # SQL query to retrieve data
   cursor.execute('''SELECT * FROM Books''')
   rows = cursor.fetchall()

   with open('books.csv', 'w') as file:
      writer = csv.writer(file)
      writer.writerow(['ID', 'Title', 'Author', 'Qty'])
      writer.writerows(rows)       
   print("Data has been saved to books.csv")



# Main program
def main():
    #Call fun to create the book database-i.e. connection with sqlite
    db = create_database()
    #create the cursor object
    cursor = db.cursor() 
    while True:
      user_choice = int(input(usage_message))
      if user_choice == 1:
        add_book(cursor)
        db.commit()
      elif user_choice == 2:
        update_book(cursor)
        db.commit()
      elif user_choice == 3:
        delete_book(cursor)
        db.commit()
      elif user_choice == 4:
        search_book(cursor)
      elif user_choice == 5:
        view_bookdb(cursor)
      elif user_choice == 6:
        savedb_csv(cursor,db)
      elif user_choice==0:
          print("Closing the db now!")
     
          # SQL code that will delete all the data in the table, but not the table
          # Delete all data inside the Student table
          #cursor.execute('DELETE FROM Books')
          #db.commit()
          
          db.close()
          break
      else:
            print("Invalid choice. Please try again.")
         
         

if __name__ == "__main__":
    main()



