from get_datapoints import *
from get_experiment import *
from get_metadata import *
from hierarchy_lists import *
import sys

def main():
    """Exports data to a YAML file."""

    author_info = get_author_info()
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
