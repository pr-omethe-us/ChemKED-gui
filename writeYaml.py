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
apparatus = input("Apparatus: ")
kind = input("Kind: ")
institution = input("Institution: ")
facility = input("Facility: ")
