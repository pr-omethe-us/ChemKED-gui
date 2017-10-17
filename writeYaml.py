import yaml

def represent_mapping(self, tag, mapping, flow_style=None):
    # This fix doesn't work.
    # Potential solutions:
    # -Remove line from yaml module and include
    #  modified yaml module in the gui module.
    # -Write the data line-by-line? (Seems inefficient)
    # -Somehow have yaml call this modified function
    #  instead of the one built into the yaml module.
    """This is a modified pyyaml function.
    The mapping.sort() line has been commented out
    so as to preserve the order of items as they are
    written to the yaml file."""
    value = []
    node = MappingNode(tag, value, flow_style=flow_style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    best_style = True
    if hasattr(mapping, 'items'):
        mapping = mapping.items()
        # mapping.sort()
    for item_key, item_value in mapping:
        node_key = self.represent_data(item_key)
        node_value = self.represent_data(item_value)
        if not (isinstance(node_key, ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))
    if flow_style is None:
        if self.default_flow_style is not None:
            node.flow_style = self.default_flow_style
        else:
            node.flow_style = best_style
    return node


def get_author_info():
    print("File Author Information")

    author_name = input("Author Name: ")
    orcid = input("ORCID: ")

    file_version = input("File Version: ")
    chemked_version = input("ChemKED Version: ")

    return author_name, orcid, file_version, chemked_version


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


def get_datapoints():
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


def main():
    """Exports data to a YAML file."""
    author_info = get_author_info()
    # reference_info = get_reference_info()
    # get_experiment_info()
    # get_common_properties_info()
    # get_datapoints()

    data = {"file-author": {"name": author_info[0], "ORCID": author_info[1]},
            "file-version": author_info[2],
            "chemked-version": author_info[3]
            }

    with open('data.yaml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


if __name__ == "__main__":
    main()
