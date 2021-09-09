import sys
from os import listdir, system


def main(args):
    if len(args) == 2:
        if args[1].lower() == "-service":
            _filename_parser("service")
        elif args[1].lower() == "-deploy":
            _filename_parser("deploy")
        elif args[1].lower() == "-all":
            _filename_parser("all")
        else:
            print(
                f"Add flags when starting this script.\n\n\tPossible flags:\n\t\tpython {args[0]} -deploy\n\t\tpython {args[0]} -service\n\t\tpython {args[0]} -all\n\t\tpython {args[0]} -h/-help")
    else:
        print(
            f"Add flags when starting this script.\n\n\tPossible flags:\n\t\tpython {args[0]} -deploy\n\t\tpython {args[0]} -service\n\t\tpython {args[0]} -all\n\t\tpython {args[0]} -h/-help")


def _filename_parser(flag):
    files = listdir()
    files = [file for file in files if ".yaml" in file]
    yaml_type = {"service": [], "deploy": [], "all": []}

    for file in files:
        if "service" in file:
            yaml_type["service"].append(file)
        else:
            yaml_type["deploy"].append(file)

        yaml_type["all"].append(file)

    agent(yaml_type[flag])


def agent(filenames):

    for filename in filenames:
        print(f"> kubectl apply -f .\\{filename}\\")
        #system(f'cmd /k "kubectl apply -f .\\{filename}\\"')


if __name__ == "__main__":
    args = sys.argv
    available_flags = ["-deploy", "-service", "-all", "-h", "-help"]
    main(args)
