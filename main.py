from hierarchy_lists import *
# import sys


def get_author_info():
    print("File/Author Information")

    file_name = input("Filename: ")

    author_name = input("Author Name: ")
    orcid = input("ORCID: ")

    file_version = input("File Version: ")
    chemked_version = input("ChemKED Version: ")

    return file_name, author_name, orcid, file_version, chemked_version


def get_experiment_info():
    print("Experiment Information")

    experiment_type = input("Experiment Type: ")

    print("Apparatus Information")

    kind = input("Kind: ")
    institution = input("Institution: ")
    facility = input("Facility: ")

    return experiment_type, kind, institution, facility


def get_common_properties_info():
    print("Common Properties Information")
    # Ask Weber about formatting here


def get_reference_info():
    print("Reference Information")

    doi = input("DOI: ")
    # Need to check how many authors there are first.
    authors = input("Authors (comma-separated): ")
    journal = input("Journal: ")
    year = input("Year: ")
    volume = input("Volume: ")
    pages = input("Pages: ")
    detail = input("Detail: ")

    return doi, authors, journal, year, volume, pages, detail


def get_datapoints():
    """
    Returns a list containing lists.
    Each sublist contains experimental
    data for one datapoint.
    """

    print("Datapoints Information")

    num_datapoints = int(input("How many datapoints? "))
    # confirm = input(" ".join(["Is", num_datapoints, "correct? (y/n)"]))
    datapoints = []

    for i in range(num_datapoints):
        print("Datapoint {}".format(i + 1))

        temperature = input("Temperature (K): ")
        ignition_delay = input("Ignition Delay (us): ")
        pressure = input("Pressure (atm): ")
        # Ask Weber about the following:
        # composition, ignition type
        equivalence_ratio = input("Equivalence Ratio: ")
        # Add composition, ignition type to following list:
        datapoint = [temperature, ignition_delay, pressure,
                     equivalence_ratio]
        datapoints.append(datapoint)

    return datapoints

hierarchy_0 = [
    'file-author:',
    'file-version:',
    'chemked-version:',
    'reference:',
    'experiment-type:',
    'apparatus:',
    'common-properties:',
    'datapoints:'
]

hierarchy_file_author = [
    'name',
    'ORCID'
]

hierarchy_reference = [
    'doi',
    'authors',
    'journal',
    'year',
    'volume',
    'pages',
    'detail',
]

hierarchy_apparatus = [
    'kind',
    'institution',
    'facility'
]

hierarchy_common_properties = [
    'composition',
    'ignition-type'
]


def main():
    """Exports data to a YAML file."""

    # author_info = get_author_info()
    # reference_info = get_reference_info()
    # get_experiment_info()
    # get_common_properties_info()
    # get_datapoints()
    f = open('testwrite.txt', 'w+')

    for header in hierarchy_0:
        f.write(header)
        f.write('\n')

    for line in f:
        print(line)

    f.close()


if __name__ == "__main__":
    main()
