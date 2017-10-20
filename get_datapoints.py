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
