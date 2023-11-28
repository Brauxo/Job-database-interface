#project : Database of jobs with searching , sorting and more ! 2023
import tkinter as tk

#import JobDatabase 
from JobDatabase import JobDatabase

#import Interface
from Interface import Interface

#neet to be installed pip install sv-ttk
import sv_ttk




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