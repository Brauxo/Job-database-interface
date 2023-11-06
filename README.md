# Jobs Database Application by Brauxo 2023
This repository contains a Python application built with Tkinter for managing and viewing a database of job listings. The application includes functionalities like searching, sorting, and filtering based on different criteria.

[Access here !](PROJET_Jobschecker.py)

## Features
Database Generation : The application generates a database of job listings with randomly assigned names, descriptions, locations, sectors, and salaries.

Display and Interaction : The Tkinter Treeview widget is used to display the job database, allowing users to interact with the displayed data.

Search Functionality : Users can search for jobs by entering keywords in the search bar. Jobs are filtered based on the job names.

Sorting Capability : The app enables users to sort the displayed job database based on the columns (such as ID, Name, Description, Location, Sector, and Salary) by clicking on the respective column headers.

Salary Filter : Users can apply a filter for job listings based on the desired salary range by entering the minimum and maximum salary values.

Combined Search and Salary Filter: An option is available to apply both the search and salary filters simultaneously.

Add job : you can add jobs one by one using the add job feature.

New file, open file, save file : you can save your progress using the menu toolbar

generate random jobs : In the menu you can find a generator that will create 30 randoms jobs from a preset list

## Instructions
To use the application:

Run the Python script on an IDE (VScode for preference). 
After that you can :
	>Go to the menu and create a new file or use the preset database.
	>Use the search bar to find jobs based on keywords.
	>Click on the column headers in the displayed job listings to sort the data.
	>Enter the minimum and maximum salary values to apply a salary filter.
	>Activate the option to apply both the search and salary filters at once.
	>At the end you can save your progress by using the menu.

## It needs :
Python 3.x
Tkinter
Random library
Regular expressions (re) library
CSV format