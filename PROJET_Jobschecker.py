#project : Database of jobs with searching , sorting and more ! 2023
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv
import re
import random
from pathlib import Path
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk

#neet to be installed pip install sv-ttk
import sv_ttk

#The first part is used to generate a databse of jobs :

class JobDatabase:
    def __init__( self ) :
        # Sectors of jobs
        self.sectors = ["Technology", "Healthcare", "Finance", "Education", "Art", "Military", "Marketing", "Industrial"]

        # locations possibles
        self.locations = ["Prague", "Brno", "Ostrava", "Plzen" ,"Liberec", "Olomouc","Abroad"]

        #jobs name possible
        self.name = ["Engineer","Developer","CEO","Technician","Worker","Salesman" ,"Searcher","Security","Comedian","Tester"]

        #descriptions possible 
        self.descriptions = [
            "Need to be someone that can be trusted.",
            "Able to understand hard topics.",
            "Working with a lot of people.",
            "Require Patience and skill.",
            "Never be late at work.",
            "Create new strategies for the service.",
            "Designing skills are required.",
            "Create advanced visual concepts.",
            "Understanding of the clients.",
        ]
        
        # create 30 jobs 
        self.database_jobs = self.generate_random_database_jobs(30)

    # Generate a random database of jobs
    def generate_random_database_jobs(self,number):
        list_jobs = []
        for i in range(number):
            job = { "id": i + 1, "Name": random.choice(self.name), "Description": random.choice(self.descriptions), "Location": random.choice(self.locations), "Sector": random.choice(self.sectors), "Salary CZK": random.randint(20000, 100000) }
            list_jobs.append(job) #add the job in the list
        return list_jobs
    




# here we create the interface and functions that will be used  :
class Interface:
    # init the jobinterface and global variables
    def __init__(self, win, job_db):
        self.win = win
        self.job_db = job_db #the database where we will have the list of jobs and their infos


        # Variables used
        self.entry_search = ttk.Entry(win, width=100)
        self.set_min_salary = ttk.Entry(win)
        self.set_max_salary = ttk.Entry(win)

        self.treeview = None  # the treeview that will be used
        self.init_treeview()
        self.create_interface()
        




        # the interface using tkinter :
    def create_interface(self):
        # Title of the app
        self.win.title("Jobschecker")

        # Adding text at the top
        ttk.Label(self.win, text="Welcome to Jobschecker: the app to search Jobs!").grid(column=0, row=0)
        ttk.Label(self.win, text="BRAUX Owen 2023").grid(column=0, row=1)

        # Search bar
        self.entry_search.grid(column=0, row=2)
        # Search button for the search bar
        ttk.Button(self.win, text="Search", command=self.search_jobs).grid(column=1, row=2)

        # Button to add jobs
        ttk.Button(self.win, text="Add Job", command=self.add_job).grid(column=0, row=5, columnspan=3)

        # buttons for the salary filter
        ttk.Label(self.win, text="Minimum salary:").grid(row=0, column=4)
        self.set_min_salary.grid(row=0, column=5)

        ttk.Label(self.win, text="Maximum salary:").grid(row=1, column=4)
        self.set_max_salary.grid(row=1, column=5)

        ttk.Button(self.win, text="Enter filters", command=self.apply_salary_filter).grid(row=1, column=6)

        # button to activate both filters
        radVar = tk.IntVar()
        ttk.Checkbutton(self.win, text="Search and salary filters", variable=radVar, command=self.bothfilter).grid(column=5, row=3)

        
        ttk.Button(self.win, text="Show Graph", command=self.show_graph).grid(row=6, column=0, columnspan=3)

        # Display all jobs initially
        self.display_jobs(self.job_db.database_jobs)

        # Menu of the app
        menubar1 = tk.Menu(self.win)
        menu1 = tk.Menu(menubar1, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label="New", command=self.new_file)
        menu1.add_command(label="Open", command=self.open_file)
        menu1.add_command(label="Save as", command=self.save_file)
        menu1.add_separator()
        menubar1.add_cascade(label="New/Open/Save File", menu=menu1)
        menubar1.add_command(label="Generate jobs", command=self.generator)
        menubar1.add_command(label="Exit the app", command=self.win.quit)

        # display the menu
        self.win.config(menu=menubar1)

    # Initialize treeview 
    def init_treeview(self) :
        # I use Treeview from tkinter to display the list of jobs
        columns = ("ID", "Name", "Description", "Location", "Sector", "Salary CZK")
        self.treeview = ttk.Treeview(self.win, columns=columns, show="headings")
        for col in columns:
            self.treeview.heading(col, text=col, command=lambda c=col: self.sort_column(c)) #this line is used to sort when you click a column
            if col == "Description":
                self.treeview.column(col, width=300)  # Description is long so it needs to take more place
            else:
                self.treeview.column(col, width=80)  # other columns
        self.treeview.grid(column=0, row=3, columnspan=2)


    # Function to display the database of jobs in the treeview
    def display_jobs(self,jobs):
        for job in jobs:
            self.treeview.insert("", "end", values=(job['id'], job['Name'], job['Description'], job['Location'], job['Sector'], job['Salary CZK'])) #insert line by line

    # Function to clear the treeview
    def clear(self):
        for lines in self.treeview.get_children():
            self.treeview.delete(lines) #delete line by line 

    # Function to search for jobs based on a keyword (could be improved)
    def search_jobs(self):
        keyword = self.entry_search.get().lower() 
        searching = []
        for job in self.job_db.database_jobs : # job_db is the name of our database in Main
            if re.search(keyword, job['Name'].lower()):
                searching.append(job)
        self.clear()#remove the old treeview
        self.display_jobs(searching)


    # function used to sort the column in alphabetical orders or by number 
    def sort_column(self,col):
        info_of_column = []
        for child in self.treeview.get_children(''):
            val = self.treeview.set(child, col)
            info_of_column.append((val, child))
        info_of_column.sort()
        for index, (val, child) in enumerate(info_of_column):
            self.treeview.move(child, '', index)


    # Function to add a job to the database
    def add_job(self):
        # this function is used to add the new job in the database : 
        def add_to_database():
            newjob = { "id": len(self.job_db.database_jobs) + 1, "Name": newname.get(), "Description": newdescription.get(), "Location": newlocation.get(), "Sector": newsector.get(), "Salary CZK": int(newsalary.get()) }
            self.job_db.database_jobs.append(newjob)
            self.display_jobs([newjob])  # Display only the new job, not all jobs
            addjob_interface.destroy() #destroy the addjob interface


        addjob_interface = tk.Toplevel(self.win)
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
        newsector = ttk.Combobox(addjob_interface, values=self.job_db.sectors)
        newsector.grid(row=2, column=3)

        ttk.Label(addjob_interface, text="Salary CZK:").grid(row=3, column=0)
        newsalary = ttk.Entry(addjob_interface)
        newsalary.grid(row=3, column=1)

        #button that add the job to the database
        add_button = ttk.Button(addjob_interface, text="Add Job", command=add_to_database) 
        add_button.grid(row=4, column=0, columnspan=4)


    # filters jobs with a wanted salary
    def filter_salary(self,minimum, maximum):
        validjobs = []
        for job in self.job_db.database_jobs :
            if minimum <= job['Salary CZK'] <= maximum :
                validjobs.append(job)
        self.clear()
        self.display_jobs(validjobs)


    # this apply a filter for the salary
    def apply_salary_filter(self):
        try:
            min_salary = int(self.set_min_salary.get())
            max_salary = int(self.set_max_salary.get())
            self.filter_salary(min_salary, max_salary)
        except :
            # Notify the user of incorrect input
            print("these salaries are not possible !")

    # toggle search and salary filter by reusing both code (not the best method but w/e)
    def bothfilter(self):
            try:
                min_salary = int(self.set_min_salary.get())
                max_salary = int(self.set_max_salary.get())
                keyword = self.entry_search.get().lower() 
                filteresearch = []
                for job in self.job_db.database_jobs:
                    if min_salary <= job['Salary CZK'] <= max_salary and re.search(keyword, job['Name'].lower()):
                        filteresearch.append(job)
                self.clear()#remove the old treeview
                self.display_jobs(filteresearch)
            except :
                print("Recheck the values!")

    
     # create a new empty list of job
    def new_file(self) :
        self.job_db.database_jobs = []  # Clears the existing jobs data or creates an empty list
        self.clear()  # Clears the displayed jobs in the interface

    # open a file (list of jobs) #very buggy and could be improved 
    def open_file(self) :
        path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            with open(path, 'r') as file :
                readthefile = csv.reader(file)
                joblist = []
                for line in readthefile :
                    try:
                        job = { "id": int(line[0]), "Name": line[1], "Description": line[2], "Location": line[3], "Sector": line[4], "Salary CZK": int(line[5]) }
                        joblist.append(job)
                    except :
                        print("Impossible to open the file !")
            self.job_db.database_jobs = joblist
            self.clear()
            self.display_jobs(self.job_db.database_jobs)

            

    # save the file (list of jobs)
    def save_file(self) :
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            with open(path, 'w') as file :
                savethefile = csv.writer(file)
                for job in (self.job_db.database_jobs) :
                    savethefile.writerow([job["id"], job["Name"], job["Description"], job["Location"], job["Sector"], job["Salary CZK"]])

    # generate a new list of 30 jobs !
    def generator(self) :
        new_jobs = self.job_db.generate_random_database_jobs(30)
        self.job_db.database_jobs = new_jobs
        self.clear()
        self.display_jobs(self.job_db.database_jobs)


    # show the salary distribution by sector with matplot !
    def show_graph(self):
        # Gather data for the chart
        sector_salaries = {}

        for job in self.job_db.database_jobs :
            sector = job['Sector']
            salary = job['Salary CZK']

            if sector not in sector_salaries :
                sector_salaries[sector] = []

            sector_salaries[sector].append(salary)

        # create the chart
        fig, ax = plt.subplots(figsize=(8, 6))

        for sector, salaries in sector_salaries.items():
            ax.bar(sector, sum(salaries) / len(salaries), label=sector)

        ax.set_xlabel('Sector')
        ax.set_ylabel('Average Salary CZK')
        ax.set_title('Average Salary Distribution by Sector')
        ax.legend()

        # here we display in a new window
        graphwin = tk.Toplevel(self.win)
        graphstats = FigureCanvasTkAgg(fig, master=graphwin)
        graphstats.draw()
        graphstats.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(graphstats, graphwin)
        toolbar.update()
        graphstats.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # run the interface 
    def run(self) :
        self.win.mainloop()

    #stop the program
    def stop(self):
        self.win.quit()
        self.win.destroy()



# initialisize the app
if __name__ == "__main__":

    #create a window
    win = tk.Tk()

    #icone working if you set up a path
    #win.iconbitmap(os.path.abspath("icone.ico"))


    job_db = JobDatabase()
    job_interface = Interface(win, job_db)

    #Theme used from sv_ttk
    sv_ttk.set_theme("dark")

    #protocol to stop the program 
    win.protocol("WM_DELETE_WINDOW", job_interface.stop)

    job_interface.run()


