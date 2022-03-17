from scheduler import Scheduler, Part
from countries import Countries
from resources import housing, metallic_alloys, electronics
import matplotlib.pyplot as plt
import utils
import heapq
import time

# Top level function
def my_country_scheduler(your_country_name,resources_filename,
            initial_state_filename,output_schedule_filename,
            num_output_schedules,depth_bound,
            frontier_max_size):
            transform_resources = [housing, metallic_alloys, electronics] 
            countries = Countries(your_country_name, transform_resources,
                          initial_state_filename, resources_filename)   
            scheduler = Scheduler(countries)  
            resource = scheduler.search(depth_bound, frontier_max_size)    
            print("Completed the search, now writing to the output file:")    
            for i in range(0, num_output_schedules):
                print("Schedule", i + 1)
                schedule = heapq.heappop(resource).getPartial()
                utils.write_to_file(output_schedule_filename, schedule, i + 1)
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            
                

#Randomly chose my country to be Carpania
myCountry = "Carpania"

initialStatePath = "initial_countries.xlsx"
resourcePath = "Sample-Resources.xlsx"
output = "results/example"
numberOutput = 10

timeOutputFile = open("results/runtimes.txt", "a")
# Example 1: Depth_Bound = 5 and Frontier_Max_Size = 10 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "1.txt", 
                     numberOutput, 5, 10)
finishTime = time.time()
timeOutputFile.write("The runtime for example 1 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed " + str(finishTime - startTime) + " seconds")


# Example 2: Depth_Bound = 5 and Frontier_Max_Size = 5 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "2.txt", 
                     numberOutput, 5, 5)
finishTime = time.time()
timeOutputFile.write("The runtime for example 2 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed " + str(finishTime - startTime) + " seconds")

# Example 3: Depth_Bound = 10 and Frontier_Max_Size = 5 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "3.txt",
                     numberOutput, 10, 5)
finishTime = time.time()
timeOutputFile.write("The runtime for example 3 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed: " + str(finishTime - startTime) + " seconds")

# Example 4: Depth_Bound = 15 and Frontier_Max_Size = 4 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "4.txt",
                     numberOutput, 15, 4)
finishTime = time.time()
timeOutputFile.write("The runtime for example 4 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed: " + str(finishTime - startTime) + " seconds")

# Example 5: Depth_Bound = 12 and Frontier_Max_Size = 6 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "5.txt",
                     numberOutput, 12, 6)
finishTime = time.time()
timeOutputFile.write("The runtime for example 5 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed: " + str(finishTime - startTime) + " seconds")

# Example 6: Depth_Bound = 8 and Frontier_Max_Size = 4 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "6.txt",
                     numberOutput, 8, 4)
finishTime = time.time()
timeOutputFile.write("The runtime for example 6 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed: " + str(finishTime - startTime) + " seconds")

# Example 7: Depth_Bound = 5 and Frontier_Max_Size = 8 
startTime = time.time()
my_country_scheduler(myCountry, resourcePath,
                     initialStatePath, output + "7.txt",
                     numberOutput, 5, 8)
finishTime = time.time()
timeOutputFile.write("The runtime for example 7 is " +
               str(finishTime - startTime) + " seconds")
timeOutputFile.write("\n")
print("Time elapsed: " + str(finishTime - startTime) + " seconds")




timeOutputFile.close()
