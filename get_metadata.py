def get_author_info():
    print("File/Author Information")

    file_name = input("Filename: ")

    author_name = input("Author Name: ")
    orcid = input("ORCID: ")

    file_version = input("File Version: ")
    chemked_version = input("ChemKED Version: ")

    return file_name, author_name, orcid, file_version, chemked_version


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
