import yaml

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath) as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w+") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    filepath = "/Users/michaelbernard/Documents/GitHub/ChemKED-database/2-butanol/2-butanol LPST Stranic xO2_0.03_phi_1.0.yaml"
    data = yaml_loader(filepath)
    print(data)

    items = data.get('file-author')
    for subitem in items:
        print(subitem.value)