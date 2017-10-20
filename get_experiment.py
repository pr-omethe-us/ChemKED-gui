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
