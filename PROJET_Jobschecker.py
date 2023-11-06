#project : Database of jobs with searching , sorting and more ! 2023
import tkinter as tk
from tkinter import ttk
import re
import random

#The first part is used to generate a databse of jobs :

# Sectors of jobs
sectors = ["Technology", "Healthcare", "Finance", "Education", "Art", "Military", "Marketing", "Industrial"]

# locations possibles
locations = ["Prague", "Brno", "Ostrava", "Plzen" ,"Liberec", "Olomouc"]

#jobs name possible
name = ["Engineer","Developer","CEO","Technician","Worker","Salesman" ,"searcher","security",]

#descriptions possible (I asked chat gpt to create a list of descriptions of jobs to help me)
descriptions = [
    "Responsible for developing and maintaining software applications.",
    "Analyzing and interpreting data to provide insights and recommendations.",
    "Managing financial transactions, records, and reports.",
    "Educating and instructing students in a particular field or subject.",
    "Providing customer service and ensuring guest satisfaction.",
    "Creating strategies to promote products or services.",
    "Designing, developing, and testing products or structures.",
    "Creating visual concepts to communicate ideas.",
    "Selling products or services to potential customers.",
    "Performing medical examinations and providing healthcare services.",
    "Ensuring the proper functioning of network and IT systems.",
    "Managing projects and coordinating teams to achieve objectives.",
    "Creating content for marketing and promotional purposes.",
    "Conducting research and experiments in a scientific field.",
    "Providing technical support and assistance to users.",
    "Assisting in administrative tasks and office management.",
    "Developing and implementing strategies for business growth.",
    "Operating machinery and ensuring production efficiency.",
    "Performing quality checks and ensuring product standards.",
    "Handling legal matters and providing legal advice."
]

# Generate a random database of jobs
def generate_random_database_jobs(x):
    list_jobs = []
    for i in range(x):
        job = { "id": i + 1, "Name": random.choice(name), "Description": random.choice(descriptions), "Location": random.choice(locations), "Sector": random.choice(sectors), "Salary CZK": random.randint(20000, 100000) }
        list_jobs.append(job) #add the job in the list
    return list_jobs

# create 30 jobs 
database_jobs = generate_random_database_jobs(30)


#here we create functions that will be used in the interface :

# Function to display the database of jobs in the treeview
def display_jobs(jobs):
    for job in jobs:
        treeview.insert("", "end", values=(job['id'], job['Name'], job['Description'], job['Location'], job['Sector'], job['Salary CZK'])) #insert line by line

# Function to clear the treeview
def clear():
    for lines in treeview.get_children():
        treeview.delete(lines) #delete line by line 

# Function to search for jobs based on a keyword (could be improved)
def search_jobs():
    keyword = entry_search.get().lower() 
    searching = []
    for job in database_jobs:
        if re.search(keyword, job['Name'].lower()):
            searching.append(job)
    clear()#remove the old treeview
    display_jobs(searching)


#function used to sort the column in alphabetical orders or by number 
def sort_column(col):
    info_of_column = []
    for child in treeview.get_children(''):
        val = treeview.set(child, col)
        info_of_column.append((val, child))
    info_of_column.sort()
    for index, (val, child) in enumerate(info_of_column):
        treeview.move(child, '', index)


# Function to add a job to the database
def add_job():
    #this function is used to add the new job in the database : 
    def add_to_database():
        new_job = { "id": len(database_jobs) + 1, "Name": newname.get(), "Description": newdescription.get(), "Location": newlocation.get(), "Sector": newsector.get(), "Salary CZK": int(newsalary.get()) }
        database_jobs.append(new_job)
        display_jobs([new_job])  # Display only the new job, not all jobs
        addjob_interface.destroy() #destroy the addjob interface


    addjob_interface = tk.Toplevel(win)
    addjob_interface.title("Add a Job !")

    # This is the interface that is used to create a new job

    ttk.Label(addjob_interface, text="Name:").grid(row=1, column=0)
    newname = ttk.Entry(addjob_interface)
    newname.grid(row=1, column=1)

    ttk.Label(addjob_interface, text="Description:").grid(row=1, column=2)
    newdescription = ttk.Entry(addjob_interface)
    newdescription.grid(row=1, column=3)

    ttk.Label(addjob_interface, text="Location:").grid(row=2, column=0)
    newlocation = ttk.Entry(addjob_interface)
    newlocation.grid(row=2, column=1)

    ttk.Label(addjob_interface, text="Sector:").grid(row=2, column=2)
    newsector = ttk.Combobox(addjob_interface, values=sectors)
    newsector.grid(row=2, column=3)

    ttk.Label(addjob_interface, text="Salary CZK:").grid(row=3, column=0)
    newsalary = ttk.Entry(addjob_interface)
    newsalary.grid(row=3, column=1)

    #button that add the job to the database
    add_button = ttk.Button(addjob_interface, text="Add Job", command=add_to_database) 
    add_button.grid(row=4, column=0, columnspan=4)


# filters jobs with a wanted salary
def filter_salary(minimum, maximum):
    validjobs = []
    for job in database_jobs :
        if minimum <= job['Salary CZK'] <= maximum :
            validjobs.append(job)
    clear()
    display_jobs(validjobs)


#this apply a filter for the salary
def apply_salary_filter():
    try:
        min_salary = int(set_min_salary.get())
        max_salary = int(set_max_salary.get())
        filter_salary(min_salary, max_salary)
    except :
        # Notify the user of incorrect input
        print("these salaries are not possible !")

# toggle search and salary filter by reusing both code (not the best method but w/e)
def bothfilter():
        try:
            min_salary = int(set_min_salary.get())
            max_salary = int(set_max_salary.get())
            keyword = entry_search.get().lower() 
            filteresearch = []
            for job in database_jobs:
                if min_salary <= job['Salary CZK'] <= max_salary and re.search(keyword, job['Name'].lower()):
                    filteresearch.append(job)
            clear()#remove the old treeview
            display_jobs(filteresearch)
        except :
            print("Recheck the values!")



#the interface using tkinter :


# create instance
win = tk.Tk()
# Title of the app
win.title("Jobschecker")

# Adding text at the top
ttk.Label(win ,text= "Welcome to Jobschecker : the app to search Jobs !").grid(column =0, row=0)
ttk.Label(win ,text= "BRAUX Owen 2023").grid(column =0, row=1)

# Search bar
entry_search = ttk.Entry(win, width=100)
entry_search.grid(column=0, row=2)
# Search button for the search bar
search_button = ttk.Button(win, text="Search", command=search_jobs)
search_button.grid(column=1, row=2)

#I use Treeview from tkinter to display the list of jobs
columns = ("ID", "Name", "Description", "Location", "Sector", "Salary CZK")
treeview = ttk.Treeview(win, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col, command=lambda c=col: sort_column(c)) #this line is used to sort when you click a column
    if col == "Description":
        treeview.column(col, width=300)  # Description is long so it needs to take more place
    else:
        treeview.column(col, width=80)  # other columns
treeview.grid(column=0, row=3, columnspan=2)


# Button to add jobs
add_job_button = ttk.Button(win, text="Add Job", command=add_job)
add_job_button.grid(column=0, row=5, columnspan=3)

#buttons for the salary filter
set_salary_label = ttk.Label(win, text="Minimum salary:")
set_salary_label.grid(row=0, column=4)
set_min_salary = ttk.Entry(win)
set_min_salary.grid(row=0, column=5)

set_salary_label = ttk.Label(win, text="Maximum salary:")
set_salary_label.grid(row=1, column=4)
set_max_salary = ttk.Entry(win)
set_max_salary.grid(row=1, column=5)

salary_filter_button = ttk.Button(win, text="Enter filters", command=apply_salary_filter)
salary_filter_button.grid(row=1, column=6)

#button to activate both filters
radVar = tk.IntVar()
filter_button = ttk.Checkbutton(win, text="Search and salary filters", variable=radVar, command=bothfilter)
filter_button.grid(column=5, row=3)


# Display all jobs initially
display_jobs(database_jobs)

#run the interface 
win.mainloop()