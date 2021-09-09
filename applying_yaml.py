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
    files = [file for file in files if ".yaml" in file or ".yml" in file]
    yaml_type = {"service": [], "deploy": [], "all": []}

    for file in files:
        if "service" in file:
            yaml_type["service"].append(file)
        else:
            yaml_type["deploy"].append(file)

        yaml_type["all"].append(file)

    agent(yaml_type[flag])


def agent(filenames):

    command_string = ""

    print("\nThese are the commands you will run:\n")

    for filename in filenames:
        command_string += f"kubectl apply -f {filename} & "
        print(f"\t> kubectl apply -f {filename}")

    command_string = command_string[:len(command_string)-3]

    print(
        f"\n\nAnd this is the full command that's being executed:\n\n\t{command_string}")
    inp = input("\n\nAre you sure you want to run this? (Y)/(N): ").lower()

    if inp in ["y", "yes"]:
        system(f'cmd /k "{command_string}"')
    else:
        print("Relaunch the program or try other flags if the command looked wrong!")


if __name__ == "__main__":
    args = sys.argv
    available_flags = ["-deploy", "-service", "-all", "-h", "-help"]
    main(args)
