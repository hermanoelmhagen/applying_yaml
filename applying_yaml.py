import sys
from os import listdir, system


def main(args):
    avaliable_flags = ["-service", "-deployment", "-all", "-kw"]

    if len(args) >= 2 and args[1].lower() in avaliable_flags:
        arg = args[1].lower()

        try:
            _filename_parser(arg[1:], " ".join(sys.argv[2:]))
        except:
            _filename_parser(arg[1:])

    else:
        help_message()


def help_message():
    print(
        f"Add flags when starting this script.\n\n\tPossible flags:\n\t\tpython {args[0]} -deployment\n\t\tpython {args[0]} -service\n\t\tpython {args[0]} -all\n\t\tpython {args[0]} -kw and_your_keyword_here")


def _filename_parser(flag, kw=None):
    files = listdir()
    files = [file for file in files if ".yaml" in file or ".yml" in file]
    yaml_type = {"service": [], "deployment": [], "all": [], "kw": []}

    for file in files:
        if flag in file or kw in file:
            yaml_type[flag].append(file)

        yaml_type["all"].append(file)

    agent(yaml_type[flag])


def agent(filenames):

    command_string = ""
    if len(filenames) > 0:
        print("\nThese are the commands you will run:\n")

        for filename in filenames:
            command_string += f"kubectl apply -f {filename} & "
            print(f"\t> kubectl apply -f {filename}")

        command_string = command_string[:len(command_string)-3]

        print(
            f"\n\nAnd this is the full command that's being executed:\n\n\t{command_string}")
        inp = input(
            "\n\nAre you sure you want to run this? [Y]es/[N]o: ").lower()

        if inp in ["y", "yes"]:
            system(f'cmd /k "{command_string}"')
        else:
            print("Relaunch the program or try other flags if the command looked wrong!")

    else:
        print("No files found matching your criteria :(")


if __name__ == "__main__":
    args = sys.argv
    main(args)
