import yaml
testyaml = open("/Users/michaelbernard/Documents/GitHub/ChemKED-database/2-butanol/2-butanol LPST Stranic xO2_0.03_phi_1.0.yaml", "r")
printableYaml = yaml.load(testyaml)
for line in printableYaml:
    print(line)