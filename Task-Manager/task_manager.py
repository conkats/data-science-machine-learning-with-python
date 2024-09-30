#!/usr/bin/python3
# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.
# example:https://www.geeksforgeeks.org/personalized-task-manager-in-python/
#=====importing libraries===========
import os#, fileinput
from datetime import datetime, date


#====Define the different functions====
#Create a reg_user function called when user 
#selects "r" to register a user
def reg_user(username_passwordl):
    # Check if the new password and confirmed password are the same.
    # Check if the new username already exists
     # - Request input of a new username
    new_username = input("New Username: ")
    
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")
    
    if new_username in username_password.keys():
        print("Username already exist. Please chooce a different username.") 
    else:    
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

def add_task():
    #Add the task to the user
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    #view all tasks
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine(userName):   
    #Create a function view_mine that is called when users type vm
    #to view all the tasks that have been assigned to them  
    task_count = 0
    
    for t in task_list:
        if t['username'] == userName:
            disp_str = f"Task : \t\t {t['title']}-{task_count}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            #counter of each task
            task_count =+1
              
    try:
        choice = int(input("Enter the task count to view details (or -1 to return to the menu): "))
        if choice == -1:
            print("Return to menu")
            pass  #break  # Return to the menu
        elif choice <= len(task_list[choice]):
            #note that there is a problem with the indexing of the task
            #i.e. the task choice is based on all the task indices-global
            #task_list-dictionary list
            #task_data-list
            selected_task = task_list[choice]
            print(f"Task-{choice} Details:")
            print(f"Title: {selected_task['title']}")
            print(f"Assigned to: {selected_task['username']}")
            print(f"Date Assigned: {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Due Date: {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Task Description:\t{selected_task['description']}")
            print(f"Completed:\t{selected_task['completed']}")
            #select to mark task as complete or not
            edit_choice = input("Do you want to mark as complete or edit the task? (Y/N): ").strip().lower()
            if edit_choice == 'y':
                    #check if task is yes or no
                    if selected_task['completed']==False:
                       task_list[choice]["completed"] = True
                       #open the file in write mode
                       with open("tasks.txt", "w") as task_file_update:
                            #empty list for the updated completed task
                            task_list_updated = []
                            #loop through the dictionary list to update
                            #task as completed
                            #note the last str_attris
                            for t in task_list:
                                str_attrs = [
                                    t['username'],
                                    t['title'],
                                    t['description'],
                                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                    "Yes" if t['completed'] else "No"
                                ]
                                task_list_updated.append(";".join(str_attrs))
                            task_file_update.write("\n".join(task_list_updated))
       
                       print("Task marked as complete.",)
                
            elif edit_choice == 'n':
                if not selected_task['completed']:
                    edit_option = input("Do you want to edit (U)sername or (D)ue Date? (U/D): ").strip().lower()
                    if edit_option == 'u':
                        new_username = input("Enter the new username: ")
                        selected_task['username'] = new_username
                        print("Username updated.")
                    elif edit_option == 'd':
                        new_due_date = input("Enter the new due date (YYYY-MM-DD HH:MM): ")
                        selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        print("Due date updated.")
                    else:
                        print("Task is already marked as complete and cannot be edited.")
                else:
                        print("Invalid edit option. Task not updated.")
    except ValueError:
                    print("Invalid input. Please enter a valid task number or -1 to return to the menu.")

def generate_reports(num_t):
    #empty dictionary for completed/uncompleted tasks
    t_completed = {}
    count = 0
    count_uc =0
    for t in task_list:
        if t['completed'] == True:
           count += 1  
        elif t['completed'] == False:
            count_uc +=1
        else:
            pass
        t_completed["c"] = count        
        t_completed["uc"] = count_uc
    if not os.path.exists("task_overviw.txt"):    
        with open("task_overview.txt", "w") as over_f:
            over_f.write(f"The total number of tasks:\t {num_t}\n")
            over_f.write(f"The total number of completed tasks:\t {t_completed['c']}\n")
            over_f.write(f"The total number of uncompleted tasks:\t {t_completed['uc']}\n")
            over_f.write(f"The % of uncompleted tasks:\t {(count_uc/(num_t))*100}\n")
            over_f.write(f"The % of completed tasks:\t {(count/(num_t))*100}\n")
    print("The task overview file is ready!")


#===main===
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")


# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = "admin"#input("Username: ")#"admin"
    curr_pass ="password"# input("Password: ")#
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

###########Main
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
gr - generate reports                
e - Exit
: ''').strip().lower()

    if menu == 'r':
         '''Add a new user to the user.txt file'''
         reg_user(username_password)

    elif menu == 'a':

        '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and 
         - the due date of the task.'''
        add_task()
    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all()
            
    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine(curr_user)    

    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    
    elif menu == 'gr':
         '''Generate reports of the application
         two files are produced. The task_overview.txt and
         user_overview.txt
         The user_overview.txt is the same idea so not coded here'''
         num_tasks = len(task_list)
         generate_reports(num_tasks)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
