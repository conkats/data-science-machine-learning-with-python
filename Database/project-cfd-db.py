# A program that can be used by a bookstore clerk.

import sqlite3
import csv 


usage_message = '''
# Welcome to the book system! 
# What would you like to do?

# 1 - Enter project.
# 2 - Update project.
# 3 - Delete project.
# 4 - Search projects.
# 5 - View projects in db.
# 6 - Save projects to csv. 
# For all the options use ''.
# 0 - exit this program.
'''


def create_database():
    #try:
    # Creates or opens a file called book_db 
    # with a SQLite3 DB
    db = sqlite3.connect('eproject_db')
    
    # Get a cursor object
    cursor = db.cursor()

    #Remove every trace of the table during testing
    #cursor.execute('''
    #               DROP TABLE IF EXISTS Projects
    #               ''')
    

    #rows = cursor.fetchall()
    #print("Initial data before adding any:")
    #for row in rows:
    #    print(row)
    

     # Check if table users does not exist and create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS Projects (
      ID INTEGER PRIMARY KEY,
      TITLE varchar(100),
      Author varchar(100),
      Qty int
      )''')
        # Commit the change
    db.commit()
        
    #cursor = db.cursor()

    #projects_= [(
    #     3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    #    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    #]
    #cursor.executemany('''
    #    INSERT INTO Projects (ID, 
    #                         Title, 
    #                         Author)	
    #     VALUES(?,?,?,?)''', projects_)

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

def add_project(cursor):
    id= int(input('Enter project id :\n'))
    title = input('Enter project title :\n')
    author = input('Enter project author :\n')
    cursor.execute('''INSERT INTO Projects(id, title, author)
                   VALUES(?,?,?r)''', (id, title, author)
                  )

def update_project(cursor):
    id= int(input('Enter project id to update :\n'))
    title = input('Enter new title :\n')
    author = input('Enter new author :\n')
    cursor.execute('''UPDATE Projects SET Title = ?, Author = ? 
                   WHERE ID = ?''', (title, author, id)
                  )

def delete_project(cursor):
    id= int(input('Enter project id to delete:\n'))
    cursor.execute('''DELETE FROM Projects
                    WHERE ID = ?''', (id,)
                  )

#retrieve data from sql
def search_project(cursor):
    search_term = input("Enter search term: ")
    cursor.execute('''SELECT * FROM Projects 
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

def view_projectdb(cursor):
    # Verify the deletion
    cursor.execute('SELECT * FROM Projects')
    rows = cursor.fetchall()
    print("Data after deletion:")
    for row in rows:
        print(row)

def savedb_csv(cursor,db):
   # SQL query to retrieve data
   cursor.execute('''SELECT * FROM Projects''')
   rows = cursor.fetchall()

   with open('Projects.csv', 'w') as file:
      writer = csv.writer(file)
      writer.writerow(['ID', 'Title', 'Author'])
      writer.writerows(rows)       
   print("Data has been saved to Projects.csv")



# Main program
def main():
    #Call fun to create the book database-i.e. connection with sqlite
    db = create_database()
    #create the cursor object
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



