import yaml

print("File Author Information")
author_name = input("Author Name: ")
orcid = input("ORCID: ")

file_version = input("File Version: ")
chemked_version = input("ChemKED Version: ")

print("Reference Information")
doi = input("DOI: ")
authors = input("Authors (comma-separated): ")
journal = input("Journal: ")
year = input("Year: ")
volume = input("Volume: ")
pages = input("Pages: ")
detail = input("Detail: ")

print("Experiment Information")
experiment_type = input("Experiment Type: ")
print("Apparatus Information")
kind = input("Kind: ")
institution = input("Institution: ")
facility = input("Facility: ")

#print("Common Properties Information")
#Ask Weber about formatting here

print("Datapoints Information")
num_datapoints = int(input("How many datapoints? "))
# confirm = input(" ".join(["Is", num_datapoints, "correct? (y/n)"]))
datapoints = []
for i in range(num_datapoints):
    print("Datapoint {}".format(i+1))
    temperature = input("Temperature (K): ")
    ignition_delay = input("Ignition Delay (us): ")
    pressure = input("Pressure (atm): ")
    # Ask Weber about the following:
    # composition, ignition type
    equivalence_ratio = input("Equivalence Ratio: ")
    datapoint = [temperature, ignition_delay, pressure,
                 equivalence_ratio]
    datapoints.append(datapoint)
print(datapoints)