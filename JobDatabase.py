
import random


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
    